import time
import turtle


MOVEMENT_SPEED = 3.5


class Paddle:
    def __init__(self):
        self.paddle1 = self.create_paddle(-520)
        self.paddle2 = self.create_paddle(520)

        self.is_pressed = {
            "w": False,
            "s": False,
            "Up": False,
            "Down": False
        }

        self.ball = None

    def assign_ball(self, ball):
        self.ball = ball

    @staticmethod
    def create_paddle(x):
        t = turtle.Turtle("square")
        t.penup()
        t.speed("fastest")
        t.color("white")
        t.setheading(90)
        t.goto(x, 0)
        t.shapesize(stretch_wid=0.8, stretch_len=5)
        return t

    def update_paddles(self):
        if self.is_pressed["w"]:
            self.move_paddle(self.paddle1, "up")
        if self.is_pressed["s"]:
            self.move_paddle(self.paddle1, "down")
        if self.is_pressed["Up"]:
            self.move_paddle(self.paddle2, "up")
        if self.is_pressed["Down"]:
            self.move_paddle(self.paddle2, "down")

        time.sleep(1 - ((95 + MOVEMENT_SPEED) / 100))

    def handle_keypress(self, key):
        self.is_pressed[key] = True

    def handle_keyrelease(self, key):
        self.is_pressed[key] = False

    def move_paddle(self, paddle, direction):
        if direction == "up" and paddle.ycor() < 285:
            paddle.fd(16)
        elif direction == "down" and paddle.ycor() > -285:
            paddle.bk(16)
        if paddle == self.paddle1:
            self.ball.bk(0.01)
        else:
            self.ball.fd(0.01)
