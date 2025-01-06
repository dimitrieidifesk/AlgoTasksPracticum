import turtle
import math
import time
import random


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

        current_position = self.position()
        new_position = (current_position[0] + dx, current_position[1] + dy)
        self.setposition(new_position)

    def change_direction(self, new_direction):
        self.direction = new_direction
        self.setheading(new_direction)


def get_target_point():
    edges = [
        (random.uniform(-screen_width / 2, screen_width / 2), screen_height / 2),
        (screen_width / 2, random.uniform(-screen_height / 2, screen_height / 2)),
        (random.uniform(-screen_width / 2, screen_width / 2), -screen_height / 2),
        (-screen_width / 2, random.uniform(-screen_height / 2, screen_height / 2)),
    ]
    target_point = random.choice(edges)
    return target_point


def create_turtles(num_turtles, target_point):
    turtles = []

    for i in range(num_turtles):
        name = f"Turtle_{i}"
        pond.register_shape(name, ((0, 0), (0, 20), (20, 20), (20, 0)))
        turtle_instance = MyTurtle(name, 0, 5, target_point)
        turtle_instance.penup()
        turtle_instance.goto(random.uniform(-screen_width / 4, screen_width / 4),
                             random.uniform(-screen_height / 4, screen_height / 4))
        turtle_instance.pendown()

        turtle_x, turtle_y = turtle_instance.position()
        target_x, target_y = target_point
        angle = math.degrees(math.atan2(target_y - turtle_y, target_x - turtle_x))
        turtle_instance.setheading(angle)

        turtles.append(turtle_instance)
    return turtles


if __name__ == "__main__":
    pond = turtle.Screen()
    pond.bgcolor("lightblue")
    pond.title("Pond")
    num_turtles = 2
    screen_width = pond.window_width()
    screen_height = pond.window_height()
    target_point = get_target_point()
    print(f"Цель для черепашек: {target_point}")
    turtles = create_turtles(num_turtles, target_point)
    turtle.tracer(0)
    new_target = get_target_point()
    while True:
        for turtle_instance in turtles:
            target_x, target_y = turtle_instance.target_point
            x, y = turtle_instance.position()

            # Check if the turtle reached the target point
            if math.hypot(target_x - x, target_y - y) < 5:  # Threshold for reaching the target
                if new_target == turtle_instance.target_point:
                    new_target = get_target_point()
                print(f"Новая цель для черепашеки: {turtle_instance.name}")
                turtle_instance.change_direction(
                    math.degrees(
                        math.atan2(target_point[1] - turtle_instance.ycor(), target_point[0] - turtle_instance.xcor())))
                turtle_instance.target_point = new_target
            else:
                dx = target_x - x
                dy = target_y - y
                new_direction = math.degrees(math.atan2(dy, dx))
                turtle_instance.change_direction(new_direction)

            turtle_instance.move()

        pond.update()

    turtle.done()






# def position_turtles_in_line(turtles, leader, distance):
#     for i, turtle_instance in enumerate(turtles):
#         if turtle_instance != leader:
#             angle = leader.heading()
#             dist = distance * (i + 1)
#             # distance_to_leader = turtle_instance.distance(leader)
#             # if distance_to_leader > dist:
#             #     turtle_instance.speed_value = 3
#             # elif distance_to_leader < dist:
#             #     turtle_instance.speed_value = 1
#             # else:
#             #     turtle_instance.speed_value = 2
#
#             t_x = leader.xcor() - dist * math.cos(math.radians(angle))
#             t_y = leader.ycor() - dist * math.sin(math.radians(angle))
#             new_d = math.degrees(math.atan2(t_y - turtle_instance.ycor(), t_x - turtle_instance.xcor()))
#
#             turtle_instance.change_direction(new_d)
#             print(turtle_instance.direction, new_d, turtle_instance.name)
#
#             turtle_instance.move()
#
#
# if __name__ == "__main__":
#     pond = turtle.Screen()
#     pond.bgcolor("lightblue")
#     pond.title("Pond")
#
#     num_turtles = 6
#     distance_between_turtles = 60
#     screen_width = pond.window_width()
#     screen_height = pond.window_height()
#
#     target_point = get_target_point()
#     print(f"Цель для черепашек: {target_point}")
#
#     turtles = create_turtles(num_turtles, target_point)
#     turtle.tracer(0)
#
#     while True:
#         for i, turtle_instance in enumerate(turtles):
#             if i == 0:
#                 target_x, target_y = target_point
#                 x, y = turtle_instance.xcor(), turtle_instance.ycor()
#
#                 if math.hypot(target_x - x, target_y - y) < 5:
#                     target_point = get_target_point()
#                     print(f"Новая цель для черепашек: {target_point}")
#                     turtle_instance.setheading(math.degrees(math.atan2(target_point[1] - y, target_point[0] - x)))
#                 else:
#                     dx = target_x - x
#                     dy = target_y - y
#                     turtle_instance.change_direction(math.degrees(math.atan2(dy, dx)))
#
#                 turtle_instance.move()
#             else:
#                 position_turtles_in_line(turtles, turtles[0], distance_between_turtles)
#
#         pond.update()