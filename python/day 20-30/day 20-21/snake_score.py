import time
from turtle import Turtle


FONT = ("Courier", 18, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.highscore = 0
        self.high_score()
        self.clear()
        self.hideturtle()
        self.setx(-320)
        self.sety(280)
        self.write(arg=f"Score: {self.score}", move=False, align="left", font=FONT)
        self.setx(320)
        self.sety(280)
        self.write(arg=f"High Score: {self.highscore}", move=False, align="right", font=FONT)

    def high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            self.highscore = 0

    def update_high_score(self):
        if self.score > self.highscore:
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
            self.highscore = self.score

    def points(self):
        self.clear()
        self.setx(-320)
        self.sety(280)
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align="left", font=FONT)
        self.setx(320)
        self.sety(280)
        self.write(arg=f"High Score: {self.highscore}", move=False, align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
        self.getscreen().update()
        self.update_high_score()

    def reset(self):
        self.clear()
        if self.highscore < self.score:
            self.highscore = self.score
        self.score = 0
        self.setx(-320)
        self.sety(280)
        self.write(arg=f"Score: {self.score}", move=False, align="left", font=FONT)
        self.setx(320)
        self.sety(280)
        self.write(arg=f"High Score: {self.highscore}", move=False, align="right", font=FONT)
