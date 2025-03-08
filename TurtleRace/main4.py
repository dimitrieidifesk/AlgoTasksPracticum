import turtle
import math
import random
from typing import Tuple, Dict, List
import traceback

NUM_TURTLES = 6
DISTANCE = 60
DEFAULT_SPEED = 1
TURTLE_COLORS = ["black", "white", "blue"]
AVOID_ANGLE = 90


# Прослушивание общего канала связи, через который передается сообщение о текущей целевой точки
# Каждая черепашка двигается к целевой точке самостоятельно, но надо реализовать проверку расстояния до все других черепашек во всех направлениях
# и разрешить конфликты столкновений. (Установкой вторичной целевой точки на +N градусов на несколько пикселей в сторону от ближайшей черепашки)
# Вся реализация только через пулл сообщений
# Выстроение в ряд обязательно


class Message:
    def __init__(self, id: int, cur_pos_x: float, cur_pos_y: float, cur_target: Tuple[float], direction: float):
        self.id = id
        self.cur_pos_x = cur_pos_x
        self.cur_pos_y = cur_pos_y
        self.cur_target = cur_target
        self.direction = direction


class TurtleRobot(turtle.Turtle):
    def __init__(self, name: int, initial_direction: float, speed: int,
                 cur_target_point: Tuple[float], color: str):
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

    def move(self):
        radians = math.radians(self.direction)
        dx = self.speed_value * math.cos(radians)
        dy = self.speed_value * math.sin(radians)
        self.setposition(self.xcor() + dx, self.ycor() + dy)

    def change_direction(self, new_direction):
        self.direction = new_direction
        self.setheading(new_direction)

    def avoiding_obstacles(self, new_d, closest_distance, direction_to_obstacle):
        if closest_distance < DISTANCE:
            obstacle_angle = math.degrees(math.atan2(direction_to_obstacle.cur_pos_y - self.ycor(),
                                                     direction_to_obstacle.cur_pos_x - self.xcor()))
            angle_diff = (obstacle_angle - self.direction) % 360

            distance_ratio = max(0, 1 - (closest_distance / DISTANCE))
            adaptive_angle = AVOID_ANGLE * distance_ratio * 3

            if angle_diff <= 30 or angle_diff > 330:  # Преграда спереди
                self.change_direction(new_d + adaptive_angle)  # Повернуть вбок
            elif 330 >= angle_diff > 260:  # Преграда справа
                self.change_direction(new_d - adaptive_angle)  # Повернуть влево
            elif 80 >= angle_diff > 30:  # Преграда слева
                self.change_direction(new_d - adaptive_angle)  # Повернуть вправо
            else:  # Преграда сзади
                self.change_direction(new_d)
        else:
            self.change_direction(new_d)

    def handle_messages(self, messages: List[Message]) -> Dict:
        msg_prev = None  # Сообщение от впереди идущего
        closest_distance = float('inf')
        direction_to_obstacle = None
        for i, msg in enumerate(messages):
            if msg.id == self.id:
                msg_prev = messages[i - 1]
            else:
                distance = self.distance_to(msg)
                if distance < closest_distance:
                    closest_distance = distance
                    direction_to_obstacle = msg
                    if closest_distance < DISTANCE:
                        print(f"[{self.id}] d to alive t {msg.id} = {int(closest_distance)}")

        if len(self.messages_cache) != len(messages):
            for cached_m in self.messages_cache:
                if cached_m.id not in [m.id for m in messages]:
                    self.dead_turtles_last_msgs.append(cached_m)

        for i, msg in enumerate(self.dead_turtles_last_msgs):
            distance = self.distance_to(msg)
            if distance < closest_distance:
                closest_distance = distance
                if closest_distance < DISTANCE:
                    print(f"d to dead t {msg.id} = {closest_distance}")

        self.messages_cache = messages

        if self.id == messages[0].id:
            tp = self.get_target_point_from_frame()
            if tp:
                self.setheading(math.degrees(math.atan2(tp[1] - self.ycor(), tp[0] - self.xcor())))
                self.target_point = tp
            else:
                dx = self.target_point[0] - self.xcor()
                dy = self.target_point[1] - self.ycor()
                new_d = math.degrees(math.atan2(dy, dx))
                # self.change_direction(new_d + AVOID_ANGLE if closest_distance < DISTANCE else new_d)
                self.avoiding_obstacles(new_d, closest_distance, direction_to_obstacle)
        elif msg_prev:
            angle = msg_prev.direction
            t_x = msg_prev.cur_pos_x - DISTANCE * math.cos(math.radians(angle))
            t_y = msg_prev.cur_pos_y - DISTANCE * math.sin(math.radians(angle))
            new_d = math.degrees(math.atan2(t_y - self.ycor(), t_x - self.xcor()))
            # self.change_direction(new_d + AVOID_ANGLE if closest_distance < DISTANCE else new_d)
            self.avoiding_obstacles(new_d, closest_distance, direction_to_obstacle)
            self.target_point = msg_prev.cur_target if self.target_point != msg_prev.cur_target else self.target_point
        return Message(self.id, self.xcor(), self.ycor(), self.target_point, self.direction)

    def distance_to(self, message: Message) -> float:
        return math.sqrt((self.xcor() - message.cur_pos_x) ** 2 + (self.ycor() - message.cur_pos_y) ** 2)

    def get_target_point_from_frame(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_direction = None

        if current_x >= (screen_width / 2) - 10:  # Right
            new_direction = 180 - self.direction
        elif current_x <= (-screen_width / 2) + 10:  # Left
            new_direction = 180 - self.direction
        elif current_y >= (screen_height / 2) - 10:  # Top
            new_direction = -self.direction
        elif current_y <= (-screen_height / 2) + 10:  # Bottom
            new_direction = -self.direction

        if new_direction is not None:
            self.change_direction(new_direction)
            radians = math.radians(self.direction)
            cos_theta = math.cos(radians)
            sin_theta = math.sin(radians)

            if cos_theta > 0:
                new_target_x = screen_width / 2
            else:
                new_target_x = -screen_width / 2

            new_target_y = (new_target_x - current_x) * (sin_theta / cos_theta) + current_y

            if new_target_y > screen_height / 2:
                new_target_y = screen_height / 2
                new_target_x = (new_target_y - current_y) * (cos_theta / sin_theta) + current_x
            elif new_target_y < -screen_height / 2:
                new_target_y = -screen_height / 2
                new_target_x = (new_target_y - current_y) * (cos_theta / sin_theta) + current_x

            return (new_target_x, new_target_y)


def get_random_target_point():
    edges = [
        (random.uniform(-screen_width / 2, screen_width / 2), screen_height / 2),
        (screen_width / 2, random.uniform(-screen_height / 2, screen_height / 2)),
        (random.uniform(-screen_width / 2, screen_width / 2), -screen_height / 2),
        (-screen_width / 2, random.uniform(-screen_height / 2, screen_height / 2)),
    ]
    return random.choice(edges)


def init_turtles(num_turtles, target_point):
    turtles = []
    for i in range(num_turtles):
        name = i
        pond.register_shape(str(name), ((0, 0), (0, 20), (20, 20), (20, 0)))

        color = TURTLE_COLORS[i % len(TURTLE_COLORS)]
        new_turtle = TurtleRobot(name, 0, DEFAULT_SPEED, target_point, color)
        new_turtle.goto(random.uniform(-screen_width / 4, screen_width / 4),
                        random.uniform(-screen_height / 4, screen_height / 4))
        new_turtle.pendown()
        turtles.append(new_turtle)
    return turtles


def main():
    target_point = get_random_target_point()
    print(f"start target point {target_point}")

    turtles: List[TurtleRobot] = init_turtles(NUM_TURTLES, target_point)
    turtle.tracer(0)
    m = [Message(t.id, t.xcor(), t.ycor(), target_point, t.direction) for t in turtles]
    count = 0
    while True:
        count += 1
        if count % 1000 == 0:
            rand_t = random.randint(0, len(turtles) - 1)
            turtles[rand_t].color('red')
            del turtles[rand_t]
        m = [t.handle_messages(m) for t in turtles]
        for t in turtles:
            t.move()
        pond.update()


if __name__ == "__main__":
    pond = turtle.Screen()
    pond.bgcolor("lightblue")
    pond.title("Pond")

    screen_width = pond.window_width()
    screen_height = pond.window_height()

    main()
