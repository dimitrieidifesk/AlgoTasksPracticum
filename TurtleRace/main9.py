import turtle
import math
import random
import queue
import threading
from typing import Tuple, Dict, List
import traceback

NUM_TURTLES = 3
DISTANCE = 45
DEFAULT_SPEED = 3.9
TURTLE_COLORS = ["black", "white", "blue"]

message_queue = queue.Queue()

class Message:
    def __init__(self, id: int, cur_pos_x: float, cur_pos_y: float, cur_target: Tuple[float], direction: float,
                 progress: float = None, points_count: int = None, cur_bound: int = 0):
        self.id = id
        self.cur_pos_x = cur_pos_x
        self.cur_pos_y = cur_pos_y
        self.cur_target = cur_target
        self.direction = direction
        self.progress = progress
        self.points_count = points_count
        self.cur_bound = cur_bound


class TurtleRobot(turtle.Turtle):
    def __init__(self, name: int, initial_direction: float, speed: int,
                 cur_target_point: Tuple[float], color: str, bounds):
        super().__init__(str(name))
        self.speed(0)
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.setposition(0, 0)
        self.name = str(name)
        self.id = name
        self.direction = initial_direction
        self.speed_value = speed
        self.target_point = cur_target_point
        self.pencolor(color)
        self.messages_cache = {}
        self.dead_turtles_last_msgs = []

        self.bounds = bounds
        self.cur_bound = -1
        # self.bounds = [(-384.0, -324.0, 0.0, 324.0)]
        self.perimeter_points = self.generate_grid_points()
        self.current_perimeter_index = 0

    def generate_grid_points(self, gen_type=0) -> List[Tuple[float]]:
        global NUM_TURTLES
        points = []
        self.cur_bound += 1
        xmin, ymin, xmax, ymax = self.bounds[self.cur_bound]
        distance_between = 45
        cnt = self.id
        # for msg in self.dead_turtles_last_msgs:
        #     if msg.id <= self.id:
        #         cnt -= 1
        if not gen_type:
            x = xmin
            while x <= xmax:
                y = ymin
                if (x // distance_between) % NUM_TURTLES == self.id:
                    while y <= ymax:
                        points.append((x, y))
                        y += distance_between
                x += distance_between
        else:
            y = ymin
            while y <= ymax:
                x = xmin
                if (y // distance_between) % NUM_TURTLES == cnt:
                    while x <= xmax:
                        points.append((x, y))
                        x += distance_between
                y += distance_between
        # for point in points:
        #     self.goto(point)
        #     self.dot(5)
        # self.goto(0, 0)

        return points

    def get_distance(self, pos_y: float, pos_x: float):
        dx = self.xcor() - pos_x
        dy = self.ycor() - pos_y
        return (dx ** 2 + dy ** 2) ** 0.5

    def move(self, msg: Message):
        # Проверка на столкновения
        if msg.id != self.id:
            distance = self.get_distance(msg.cur_pos_y, msg.cur_pos_x)
            if distance < DISTANCE // 2:
                avoidance_angle = math.degrees(math.atan2(msg.cur_pos_y - self.ycor(),
                                                          msg.cur_pos_x - self.xcor()))
                self.change_direction(avoidance_angle + 90)

        radians = math.radians(self.direction)
        dx = self.speed_value * math.cos(radians)
        dy = self.speed_value * math.sin(radians)
        self.setposition(self.xcor() + dx, self.ycor() + dy)

    def change_direction(self, new_direction):
        self.direction = new_direction
        self.setheading(new_direction)

    def handle_messages(self) -> Dict:
        while True:
            try:
                message: Message = message_queue.get(timeout=0.1)
                print(message.cur_bound, message.cur_target, (int(message.cur_pos_x), int(message.cur_pos_y)), message.progress)
                if message.id != self.id:
                    tp = self.get_target_point(message)

                    if tp:
                        print(tp)
                        if tp != 'stop':
                            self.setheading(math.degrees(math.atan2(tp[1] - self.ycor(), tp[0] - self.xcor())))
                            self.target_point = tp
                    else:
                        dx = self.target_point[0] - self.xcor()
                        dy = self.target_point[1] - self.ycor()
                        self.change_direction(math.degrees(math.atan2(dy, dx)))

                    cur_progress = (self.current_perimeter_index + 1) * 100 / len(self.perimeter_points)
                    late = False

                    if abs(message.progress - cur_progress) > 1:
                        if cur_progress < message.progress and self.cur_bound == message.cur_bound:
                            self.speed_value = DEFAULT_SPEED + 0.03 * int(abs(message.progress - cur_progress)) // 10
                            late = True
                    if not late:
                        self.speed_value = DEFAULT_SPEED
                    if not tp or tp != 'stop':
                        self.move(message)
                    message_queue.put(Message(self.id, self.xcor(), self.ycor(), self.target_point, self.direction, cur_progress,
                                   len(self.perimeter_points), self.cur_bound))
                    message_queue.task_done()
                    pond.update()
            except queue.Empty:
                continue

    def run(self):
        self.handle_messages()

    def get_target_point(self, msg: List[Message]):
        # Возвращаем новую целевую точку только если мы достигли текущей
        if not self.target_point or self.distance(self.target_point) < 10:  # Если меньше 5 пикселей до цели
            if self.current_perimeter_index < len(self.perimeter_points) - 1:
                self.current_perimeter_index += 1
            else:
                if msg.progress < 98 and self.cur_bound >= msg.cur_bound:
                    print(self.id, 'stop')
                    return 'stop'
                self.perimeter_points = self.generate_grid_points(gen_type=1)
                print('new territory')
                print(self.perimeter_points)
                self.current_perimeter_index = 0
            self.target_point = self.perimeter_points[self.current_perimeter_index]
            print(self.target_point)
            return self.target_point

    def calculate_distance(self, target_point, cur_pos_x, cur_pos_y):
        dx = target_point[0] - cur_pos_x
        dy = target_point[1] - cur_pos_y
        return math.sqrt(dx ** 2 + dy ** 2)


def init_turtles(num_turtles, target_point):
    num_territories = 1
    bounds = []

    def is_overlapping(new_territory):
        for (xmin, ymin, xmax, ymax) in bounds:
            if not (new_territory[2] <= xmin or new_territory[0] >= xmax or
                    new_territory[3] <= ymin or new_territory[1] >= ymax):
                return True
        return False

    for _ in range(num_territories):
        while True:
            xmin = random.randint(-screen_width // 2, screen_width // 2 - screen_width)
            ymin = random.randint(-screen_height // 2, screen_height // 2 - screen_height)
            xmax = xmin + screen_width
            ymax = ymin + screen_height
            new_territory = (xmin, ymin, xmax, ymax)

            if not is_overlapping(new_territory):
                bounds.append(new_territory)
                break

    def draw_rectangle(xmin, ymin, xmax, ymax):
        turtle.penup()
        turtle.goto(xmin, ymin)
        turtle.pendown()
        turtle.forward(xmax - xmin)
        turtle.left(90)
        turtle.forward(ymax - ymin)
        turtle.left(90)
        turtle.forward(xmax - xmin)
        turtle.left(90)
        turtle.forward(ymax - ymin)
        turtle.left(90)

    turtle.speed(10)
    for (xmin, ymin, xmax, ymax) in bounds:
        draw_rectangle(xmin, ymin, xmax, ymax)
    # print(bounds)
    turtles = []
    for i in range(num_turtles):
        name = i
        pond.register_shape(str(name), ((0, 0), (0, 20), (20, 20), (20, 0)))

        color = TURTLE_COLORS[i % len(TURTLE_COLORS)]
        new_turtle = TurtleRobot(name, 0, DEFAULT_SPEED, target_point, color, bounds)
        new_turtle.goto(random.uniform(-screen_width / 4, screen_width / 4),
                        random.uniform(-screen_height / 4, screen_height / 4))
        new_turtle.pendown()
        turtles.append(new_turtle)
    return turtles


def main():
    global NUM_TURTLES
    turtles: List[TurtleRobot] = init_turtles(NUM_TURTLES, None)
    turtle.tracer(0)
    m = [message_queue.put(Message(t.id, t.xcor(), t.ycor(), None, t.direction, 0, 0)) for t in turtles]
    threads = []
    # message_queue.put(m[0])
    for t in turtles:
        thread = threading.Thread(target=t.run)
        threads.append(thread)
        thread.start()

    # for thread in threads:
    #     thread.join(timeout=1)
    turtle.mainloop()

if __name__ == "__main__":
    pond = turtle.Screen()
    pond.bgcolor("lightblue")
    pond.title("Pond")

    screen_width = pond.window_width()
    screen_height = pond.window_height()
    # pond.exitonclick()
    main()
