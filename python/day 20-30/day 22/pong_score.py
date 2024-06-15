from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.collision = 0
        self.clear()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 245)
        self.write(self.score1, align="center", font=("Courier", 80, "normal"))
        self.goto(60, 245)
        self.write(self.score2, align="center", font=("Courier", 80, "normal"))
        self.goto(515, -345)
        self.write(self.collision, align="center", font=("Courier", 15, "normal"))

    def point1(self):
        self.score1 += 1
        self.update_scoreboard()

    def point2(self):
        self.score2 += 1
        self.update_scoreboard()

    def collide(self):
        self.collision += 1
        self.update_scoreboard()
