import turtle


class Display:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Ping Pong")
        self.screen.setup(width=1080, height=720)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.draw_center_line()

    @staticmethod
    def draw_center_line():
        t = turtle.Turtle()
        t.penup()
        t.pensize(3)
        t.setheading(90)
        t.pencolor("white")
        t.goto(0, -360)

        while t.ycor() < 360:
            t.pendown()
            t.forward(10)
            t.penup()
            t.forward(10)
        t.hideturtle()

    def update_screen(self):
        self.screen.update()
