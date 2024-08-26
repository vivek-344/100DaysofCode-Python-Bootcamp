import turtle


class Display:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Breakout")
        self.screen.setup(width=720, height=720)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def update_screen(self):
        self.screen.update()
