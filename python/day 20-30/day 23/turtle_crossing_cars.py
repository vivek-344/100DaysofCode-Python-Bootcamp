import random
import turtle

turtle.colormode(255)
COLORS = [(213, 13, 9), (198, 12, 35), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
          (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111),
          (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161),
          (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14),
          (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]


class Cars:
    def __init__(self):
        self.cars = []
        self.speed = 0.1

    def create_car(self):
        chance = random.randint(1, 500)
        if chance == 1:
            car = turtle.Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=2, stretch_len=4)
            car.seth(180)
            x = 550
            y = random.randint(-260, 260)
            car.goto(x, y)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.fd(self.speed)

    def reset_game(self):
        for car in self.cars:
            car.goto(1000, 1000)
        self.cars.clear()

    def level_up(self):
        if self.speed < 1:
            self.speed += 0.05
