import turtle
import random
import math  # Математика для расчета движения снежков


SNOWBALLS_COUNT = 5
COLLISION_RADIUS = 30  # Радиус, в пределах которого смотрим на количество снежков
MAX_SNOWBALLS_IN_RADIUS = 3  # Максимум снежков, после которого коллизии отключаются
GRAVITY = 100  # Усиление гравитации. Уменьшил для более естественного прыжка
FRICTION = 0.99  # Коэффициент трения

SNOWBALLS_COUNT = 5  # Количество снежков
COLLISION_RADIUS = 30  # Радиус для проверки столкновений
MAX_SNOWBALLS_IN_RADIUS = 3  # Максимум снежков в радиусе для реагирования на столкновения
GRAVITY = 1  # Сила гравитации
FRICTION = 0.00098  # Коэффициент трения для замедления
BOUNCE_FACTOR = 0.99  # Коэффициент отскока, который уменьшает скорость после удара о землю
GROUND_LEVEL = -50  # Уровень "земли", где снежки будут отскакивать

class Snowball:
    def __init__(self, x, y, speed, angle, color="white", size=10):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.color = color
        self.size = size  # Размер снежка
        self.vertical_speed = random.uniform(5, 15)  # Вертикальная начальная скорость для прыжка (положительная!)

        # Создаем снежок как объект Turtle
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color(self.color)
        self.ball.shapesize(stretch_wid=self.size / 10)
        self.ball.speed(0)
        self.ball.penup()
        self.ball.goto(self.x, self.y)

    def move(self):
        # Обновляем вертикальное движение под действием гравитации
        self.vertical_speed -= GRAVITY  # Уменьшение вертикальной скорости из-за гравитации
        self.y += self.vertical_speed  # Движение вверх/вниз

        # Обновляем горизонтальное движение
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.speed *= FRICTION  # Замедляем горизонтальную скорость из-за трения

        # Проверяем границы экрана и "отскок" от стенок
        if self.x < -290 or self.x > 290:  # Если снежок наталкивается на стену
            self.angle = 180 - self.angle  # Меняем направление движения по горизонтали
            self.speed *= 0.9  # Уменьшаем скорость после столкновения со стеной

        # Проверяем столкновение с "полом"
        if self.y <= GROUND_LEVEL:
            self.y = GROUND_LEVEL  # Фиксируем снежок на уровне земли
            self.vertical_speed = -self.vertical_speed * BOUNCE_FACTOR  # Уменьшаем скорость отскока
            if abs(self.vertical_speed) < 1:  # Если скорость отскока слишком мала
                self.vertical_speed = 0  # Останавливаем снежок
                self.speed = 0  # Горизонтальная скорость тоже обнуляется

        self.ball.setposition(self.x, self.y)

    def check_collision(self, other):
        # Проверяем столкновение с другим снежком
        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if dist < self.size + other.size:  # Если расстояние меньше суммы радиусов
            # Меняем направления движения двух снежков
            temp_angle = self.angle
            self.angle = other.angle
            other.angle = temp_angle
            self.speed, other.speed = other.speed, self.speed  # Меняем скорости снежков


def main():
    line_pen = turtle.Turtle()
    line_pen.hideturtle()
    line_pen.speed(0)
    line_pen.penup()
    line_y = -50
    line_pen.goto(-280, line_y)
    line_pen.pendown()
    line_pen.goto(280, line_y)

    snowballs = []
    for _ in range(SNOWBALLS_COUNT):  # Создаем снежки
        angle = random.randint(0, 360)
        snowball = Snowball(0, line_y + 10, speed=2, angle=angle)
        snowballs.append(snowball)

    while True:
        for snowball in snowballs:
            snowball.move()

        for i in range(len(snowballs)):
            count_nearby = 0
            for j in range(len(snowballs)):
                if i != j:
                    dist = math.sqrt((snowballs[i].x - snowballs[j].x) ** 2 + (snowballs[i].y - snowballs[j].y) ** 2)
                    if dist < COLLISION_RADIUS:  # Если снежки в пределах радиуса
                        count_nearby += 1

            if count_nearby < MAX_SNOWBALLS_IN_RADIUS:  # Проверяем, действительно ли нужно проверять столкновения
                for j in range(i + 1, len(snowballs)):
                    snowballs[i].check_collision(snowballs[j])

        turtle.update()  # Обновляем экран после движения всех снежков
        turtle.delay(20)  # Задержка для плавности движения, например 20 миллисекунд


screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.tracer(0)
screen.title("Pond")
screen.setup(width=600, height=600)  # Установка размера окна

if __name__ == "__main__":  # Исправлено имя модуля
    main()
    turtle.done()
