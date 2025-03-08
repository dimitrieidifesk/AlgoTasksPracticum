import turtle as t
import random
import math
import time

grav = 0.5
energ = 0.9
gr = -300
R = 10
dist = 25
SNOWBALLS_COUNT = 20
SCREEN_WIDTH = 600

class Snowball:
    def __init__(self, x=0, y=gr):
        self.snowball = t.Turtle()
        self.snowball.shape("circle")
        self.snowball.color("white")
        self.snowball.penup()
        self.snowball.goto(x, y)
        self.snowball.speed(0)
        self.radius = R

        self.x_speed = random.uniform(-5, 5)
        self.y_speed = random.uniform(10, 20)

    def move(self, snowballs):
        x, y = self.snowball.xcor(), self.snowball.ycor()
        self.y_speed -= grav
        x += self.x_speed
        y += self.y_speed

        if y <= gr:
            y = gr
            self.y_speed = -self.y_speed * energ
            if abs(self.y_speed) < 1:
                self.y_speed = 0
                self.x_speed = 0

        if x - self.radius <= -SCREEN_WIDTH // 2 or x + self.radius >= SCREEN_WIDTH // 2:
            self.x_speed = -self.x_speed * energ
            if x - self.radius <= -SCREEN_WIDTH // 2:
                x = -SCREEN_WIDTH // 2 + self.radius
            if x + self.radius >= SCREEN_WIDTH // 2:
                x = SCREEN_WIDTH // 2 - self.radius

        for other in snowballs:
            if other != self and self.is_colliding(other):
                self.handle_collision(other)
                self.separate_snowballs(other)

        self.snowball.goto(x, y)

    def is_colliding(self, other):
        distance = math.sqrt(
            (self.snowball.xcor() - other.snowball.xcor()) ** 2 + (self.snowball.ycor() - other.snowball.ycor()) ** 2)
        return distance <= (self.radius + other.radius)

    def handle_collision(self, other):
        dx = other.snowball.xcor() - self.snowball.xcor()
        dy = other.snowball.ycor() - self.snowball.ycor()

        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return

        nx = dx / distance
        ny = dy / distance

        dvx = self.x_speed - other.x_speed
        dvy = self.y_speed - other.y_speed

        dp = dvx * nx + dvy * ny

        impulse = 2 * dp / (1 + 1)

        self.x_speed -= impulse * nx
        self.y_speed -= impulse * ny
        other.x_speed += impulse * nx
        other.y_speed += impulse * ny

    def separate_snowballs(self, other):
        dx = other.snowball.xcor() - self.snowball.xcor()
        dy = other.snowball.ycor() - self.snowball.ycor()

        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return

        separation = (self.radius + other.radius + dist) - distance
        if separation > 0:
            nx = dx / distance
            ny = dy / distance

            self.snowball.goto(self.snowball.xcor() - separation / 2 * nx, self.snowball.ycor() - separation / 2 * ny)
            other.snowball.goto(other.snowball.xcor() + separation / 2 * nx,
                                other.snowball.ycor() + separation / 2 * ny)

    def is_stopped(self):
        return self.x_speed == 0 and self.y_speed == 0

def main():
    screen = t.Screen()
    screen.bgcolor("lightblue")
    screen.tracer(0)
    screen.title("Snowballs")
    screen.setup(width=SCREEN_WIDTH, height=700)

    snowballs = []
    for _ in range(SNOWBALLS_COUNT):
        x = random.uniform(-100, 100)
        snowballs.append(Snowball(x=x))

    running = True
    while running:
        running = False
        for snowball in snowballs:
            snowball.move(snowballs)
            if not snowball.is_stopped():
                running = True

        screen.update()
        time.sleep(0.02)

    screen.mainloop()

if __name__ == "__main__":
    main()
