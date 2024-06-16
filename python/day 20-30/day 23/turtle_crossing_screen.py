import turtle


class Display:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Turtle Crossing")
        self.screen.setup(width=1080, height=720)
        self.screen.tracer(0)
