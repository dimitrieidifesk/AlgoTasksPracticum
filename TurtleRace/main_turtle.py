import turtle
import math
import random
from typing import Tuple
import traceback

NUM_TURTLES = 4
DISTANCE = 50
DEFAULT_SPEED = 5
TURTLE_COLORS = ["black", "white"]

# Прослушивание общего канала связи, через который передается сообщение о текущей целевой точки
# Каждая черепашка двигается к целевой точке самостоятельно, но надо реализовать проверку расстояния до все других черепашек во всех направлениях
# и разрешить конфликты столкновений. (Установкой вторичной целевой точки на +N градусов на несколько пикселей в сторону от ближайшей черепашки)
# Вся реализация только через пулл сообщений
# Выстроение в ряд обязательно

class TurtleRobot(turtle.Turtle):
    def __init__(self, name: str, initial_direction: float, speed: int,
                 cur_target_point: Tuple[float], color: str):
        super().__init__(name)
        self.speed(0)
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.setposition(0, 0)
        self.name = name
        self.direction = initial_direction
        self.speed_value = speed
        self.target_point = cur_target_point
        self.pencolor(color)

    def move(self):
        radians = math.radians(self.direction)
        dx = self.speed_value * math.cos(radians) / 10
        dy = self.speed_value * math.sin(radians) / 10
        self.setposition(self.xcor() + dx, self.ycor() + dy)

    def change_direction(self, new_direction):
        self.direction = new_direction
        self.setheading(new_direction)

    def receive_message(self, direction=None, prev_robot = None):
        if direction is not None:
            print(f"[{self.name}] Receive {self.direction}")
            # self.change_direction(direction)
            self.process_message(direction, prev_robot)

    def send_message(self):
        if self.next_turtle is not None:
            # print(f"Send {self.direction} to {self.next_turtle.name}")
            self.next_turtle.receive_message(self.direction, self)

    def process_message(self, direction, prev_robot):
        pred_x = prev_robot.xcor()
        pred_y = prev_robot.ycor()
        angle = prev_robot.heading()

        t_x = pred_x - DISTANCE * math.cos(math.radians(angle))
        t_y = pred_y - DISTANCE * math.sin(math.radians(angle))
        new_d = math.degrees(math.atan2(t_y - self.ycor(), t_x - self.xcor()))
        self.change_direction(new_d)
        self.move()
        self.send_message()

    def target_move(self):
        target_x, target_y = self.target_point
        angle = math.degrees(math.atan2(target_y - self.ycor(), target_x - self.xcor()))
        self.change_direction(angle)
        self.move()


def get_random_target_point():
    edges = [
        (random.uniform(-screen_width / 2, screen_width / 2), screen_height / 2),
        (screen_width / 2, random.uniform(-screen_height / 2, screen_height / 2)),
        (random.uniform(-screen_width / 2, screen_width / 2), -screen_height / 2),
        (-screen_width / 2, random.uniform(-screen_height / 2, screen_height / 2)),
    ]
    return random.choice(edges)


def get_target_point_from_frame(turtle_instance):
    current_x = turtle_instance.xcor()
    current_y = turtle_instance.ycor()
    new_direction = None

    if current_x >= (screen_width / 2) - 10:  # Right
        new_direction = 180 - turtle_instance.direction
    elif current_x <= (-screen_width / 2) + 10:  # Left
        new_direction = 180 - turtle_instance.direction
    elif current_y >= (screen_height / 2) - 10:  # Top
        new_direction = -turtle_instance.direction
    elif current_y <= (-screen_height / 2) + 10:  # Bottom
        new_direction = -turtle_instance.direction

    if new_direction is not None:
        turtle_instance.change_direction(new_direction)
        radians = math.radians(turtle_instance.direction)
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


def init_turtles(num_turtles, target_point):
    turtles = []
    for i in range(num_turtles):
        name = f"turtle_{i}"
        pond.register_shape(name, ((0, 0), (0, 20), (20, 20), (20, 0)))

        color = TURTLE_COLORS[i % len(TURTLE_COLORS)]
        new_turtle = TurtleRobot(name, 0, DEFAULT_SPEED, target_point, color)
        new_turtle.goto(random.uniform(-screen_width / 4, screen_width / 4),
                        random.uniform(-screen_height / 4, screen_height / 4))
        new_turtle.pendown()
        turtles.append(new_turtle)
    return turtles


def position_turtles_in_line(turtles):
    for i in range(1, len(turtles)):
        turtle_ = turtles[i]
        predecessor = turtles[i - 1]

        pred_x = predecessor.xcor()
        pred_y = predecessor.ycor()
        angle = predecessor.heading()

        t_x = pred_x - DISTANCE * math.cos(math.radians(angle))
        t_y = pred_y - DISTANCE * math.sin(math.radians(angle))
        new_d = math.degrees(math.atan2(t_y - turtle_.ycor(), t_x - turtle_.xcor()))
        turtle_.change_direction(new_d)
        turtle_.move()
        turtle_.send_message()


def find_closest_turtle(turtles, target_point):
    """Находит ближайшую черепашку к заданной точке."""
    closest_turtle = None
    min_distance = float('inf')

    for turtle in turtles:
        distance = math.sqrt((turtle.xcor() - target_point[0]) * 2 + (turtle.ycor() - target_point[1]) * 2)

        if distance < min_distance:
            min_distance = distance
            closest_turtle = turtle

    return closest_turtle

def main_loop():
    target_point = get_random_target_point()
    print(f"start target point {target_point}")

    turtles = init_turtles(NUM_TURTLES, target_point)
    turtle.tracer(0)
    try:
        while True:
            head_turtle = find_closest_turtle(turtles, target_point)
            target_x, target_y = target_point
            x, y = head_turtle.xcor(), head_turtle.ycor()

            tp = get_target_point_from_frame(head_turtle)
            if tp:
                target_point = tp
                head_turtle.setheading(math.degrees(math.atan2(target_point[1] - y, target_point[0] - x)))
            else:
                dx = target_x - x
                dy = target_y - y
                head_turtle.change_direction(math.degrees(math.atan2(dy, dx)))
            head_turtle.send_message()
            head_turtle.move()

            pond.update()

    except Exception:
        print(traceback.format_exc())
    finally:
        turtle.done()


if __name__ == "__main__":
    pond = turtle.Screen()
    pond.bgcolor("lightblue")
    pond.title("Pond")

    screen_width = pond.window_width()
    screen_height = pond.window_height()

    main_loop()
