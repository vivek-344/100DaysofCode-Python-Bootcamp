import turtle


class Utilities(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,0)

    def game_over(self):
        self.clear()
        self.color("red")
        self.write("Game Over", align="center", font=("Courier", 24, "bold"))

    def level_up(self):
        self.clear()
        self.color("green")
        self.write("Level Up!", align="center", font=("Courier", 24, "bold"))
        turtle.ontimer(self.clear, 2000)
