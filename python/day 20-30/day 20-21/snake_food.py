import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("dark orange")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        randx = random.randint(-17, 17) * 20
        randy = random.randint(-14, 14) * 20
        self.goto(randx, randy)
