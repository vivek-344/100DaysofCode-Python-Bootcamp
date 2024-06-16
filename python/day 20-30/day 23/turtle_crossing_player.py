from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(0, -320)
        self.shapesize(2)

    def move(self):
        self.fd(5)

    def restore(self):
        self.goto(0, -320)
