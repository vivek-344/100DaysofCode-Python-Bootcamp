import turtle
import random


class Bricks:
    def __init__(self):
        self.ball = None
        self.bricks = []
        self.create_bricks()

    def assign_ball(self, ball):
        self.ball = ball

    def create_bricks(self):
        for i in range(7):
            for j in range(1, 4):
                num = random.randint(1, 3)
                if num != 1:
                    t = turtle.Turtle("square")
                    t.penup()
                    t.speed("fastest")
                    t.color("white")
                    t.goto(j * 100, (280 - (i * 30)))
                    t.shapesize(stretch_wid=1.2, stretch_len=4.5)
                    self.bricks.append(t)
                num = random.randint(1, 3)
                if num != 1:
                    t = turtle.Turtle("square")
                    t.penup()
                    t.speed("fastest")
                    t.color("white")
                    t.goto(j * -100, (280 - (i * 30)))
                    t.shapesize(stretch_wid=1.2, stretch_len=4.5)
                    self.bricks.append(t)
            num = random.randint(1, 3)
            if num != 1:
                t = turtle.Turtle("square")
                t.penup()
                t.speed("fastest")
                t.color("white")
                t.goto(0, (280 - (i * 30)))
                t.shapesize(stretch_wid=1.2, stretch_len=4.5)
                self.bricks.append(t)
