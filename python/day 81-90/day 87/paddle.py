import time
import turtle


MOVEMENT_SPEED = 3.5


class Paddle:
    def __init__(self):
        self.paddle = self.create_paddle()

        self.is_pressed = {
            "Left": False,
            "Right": False
        }

        self.ball = None

    def assign_ball(self, ball):
        self.ball = ball

    @staticmethod
    def create_paddle():
        t = turtle.Turtle("square")
        t.penup()
        t.speed("fastest")
        t.color("white")
        t.goto(0, -305)
        t.shapesize(stretch_wid=0.8, stretch_len=7)
        return t

    def update_paddles(self):
        if self.is_pressed["Left"]:
            self.move_paddle(self.paddle, "left")
        if self.is_pressed["Right"]:
            self.move_paddle(self.paddle, "right")

        time.sleep(1 - ((95 + MOVEMENT_SPEED) / 100))

    def handle_keypress(self, key):
        self.is_pressed[key] = True

    def handle_keyrelease(self, key):
        self.is_pressed[key] = False

    def move_paddle(self, paddle, direction):
        if direction == "right" and paddle.xcor() < 285:
            paddle.fd(16)
        elif direction == "left" and paddle.xcor() > -285:
            paddle.bk(16)
        if paddle == self.paddle:
            self.ball.bk(0.01)
        else:
            self.ball.fd(0.01)
