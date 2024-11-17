import turtle
import math
import random

NUM_TURTLES = 6
DISTANCE = 30
DEFAULT_SPEED = 5

class MyTurtle(turtle.Turtle):
    def __init__(self, name, initial_direction, speed, target_point):
        super().__init__(name)
        self.speed(0)
        self.shape("turtle")
        self.penup()
        self.setposition(0, 0)
        self.name = name
        self.direction = initial_direction
        self.speed_value = speed
        self.target_point = target_point

    def move(self):
        radians = math.radians(self.direction)
        dx = self.speed_value * math.cos(radians) / 10
        dy = self.speed_value * math.sin(radians) / 10
        self.setposition(self.xcor() + dx, self.ycor() + dy)

    def change_direction(self, new_direction):
        self.direction = new_direction
        self.setheading(new_direction)


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
        name = f"Turtle_{i}"
        pond.register_shape(name, ((0, 0), (0, 20), (20, 20), (20, 0)))

        t_instance = MyTurtle(name, 0, DEFAULT_SPEED, target_point)
        t_instance.goto(random.uniform(-screen_width / 4, screen_width / 4),
                        random.uniform(-screen_height / 4, screen_height / 4))
        t_instance.pendown()
        turtles.append(t_instance)
    return turtles


def get_target_point_from_frame(turtle_instance):
    current_x = turtle_instance.xcor()
    current_y = turtle_instance.ycor()

    new_direction = None

    if current_x >= (screen_width / 2) - 10:  # правая граница
        new_direction = 180 - turtle_instance.direction
        print('right', current_x, current_y, screen_width / 2, screen_height / 2)
    elif current_x <= (-screen_width / 2) + 10:  # левая граница
        new_direction = 180 - turtle_instance.direction
        print('left', current_x, current_y, screen_width / 2, screen_height / 2)
    elif current_y >= (screen_height / 2) - 10:  # верхняя граница
        new_direction = -turtle_instance.direction
        print('top', current_x, current_y, screen_width / 2, screen_height / 2)
    elif current_y <= (-screen_height / 2) + 10:  # нижняя граница
        new_direction = -turtle_instance.direction
        print('bottom', current_x, current_y, screen_height / 2, screen_height / 2)

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

    return None, None


def position_turtles_in_line(turtles, distance):
    for i in range(1, len(turtles)):
        turtle_instance = turtles[i]
        predecessor = turtles[i - 1]

        pred_x = predecessor.xcor()
        pred_y = predecessor.ycor()

        angle = predecessor.heading()

        t_x = pred_x - distance * math.cos(math.radians(angle))
        t_y = pred_y - distance * math.sin(math.radians(angle))

        new_d = math.degrees(math.atan2(t_y - turtle_instance.ycor(), t_x - turtle_instance.xcor()))
        turtle_instance.change_direction(new_d)

        turtle_instance.move()


if __name__ == "__main__":
    pond = turtle.Screen()
    pond.bgcolor("lightblue")
    pond.title("Pond")

    num_turtles = NUM_TURTLES
    distance_between_turtles = DISTANCE
    screen_width = pond.window_width()
    screen_height = pond.window_height()

    target_point = get_random_target_point()
    print(f"{target_point}")

    turtles = init_turtles(num_turtles, target_point)
    turtle.tracer(0)

    while True:
        for i, turtle_instance in enumerate(turtles):
            if i == 0:
                target_x, target_y = target_point
                x, y = turtle_instance.xcor(), turtle_instance.ycor()

                target_point_ = get_target_point_from_frame(turtle_instance)
                if all(target_point_):
                    print(target_point_)
                    target_point = target_point_
                    turtle_instance.setheading(math.degrees(math.atan2(target_point[1] - y, target_point[0] - x)))
                else:
                    dx = target_x - x
                    dy = target_y - y
                    turtle_instance.change_direction(math.degrees(math.atan2(dy, dx)))

                turtle_instance.move()

                if math.hypot(target_x - x, target_y - y) > distance_between_turtles:
                    position_turtles_in_line(turtles, distance_between_turtles)

        pond.update()

    turtle.done()
