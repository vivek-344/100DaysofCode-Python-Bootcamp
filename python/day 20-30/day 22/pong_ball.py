from turtle import Turtle
from pong_score import Score


class Ball(Turtle):
    def __init__(self, paddle1, paddle2):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.first = True
        self.up = True
        self.right = True
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.ball_speed = 3
        self.score = Score()

    def move(self):
        if self.xcor() < 0 and self.first:
            self.right = False
            self.first = False
        elif self.xcor() != 0:
            x = self.xcor()
            y = self.ycor()

            if self.distance(self.paddle1) < 50 and x < self.paddle1.xcor() + 20:
                self.right = True
                self.score.collide()
                self.increase_speed()
            if self.distance(self.paddle2) < 50 and x > self.paddle2.xcor() - 20:
                self.right = False
                self.score.collide()
                self.increase_speed()

            if y > 335:
                self.up = False
            if y < -335:
                self.up = True

            self.sety(y + self.ball_speed if self.up else y - self.ball_speed)
            self.setx(x + self.ball_speed if self.right else x - self.ball_speed)

            if self.xcor() > 515:
                self.score.point1()
                self.setx(0)
                self.right = False

            if self.xcor() < -515:
                self.score.point2()
                self.setx(0)
                self.right = True

    def increase_speed(self):
        if self.ball_speed < 10:
            self.ball_speed += 0.2
