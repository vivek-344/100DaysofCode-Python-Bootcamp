from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.clear()
        self.hideturtle()
        self.sety(280)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def points(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
