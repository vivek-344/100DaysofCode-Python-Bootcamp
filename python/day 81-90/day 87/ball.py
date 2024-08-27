from turtle import Turtle


class Ball(Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.paddle = paddle
        self.ball_speed = 3
        self.up = False
        self.right = False

    def move(self):
        x = self.xcor()
        y = self.ycor()

        top_edge = 345
        right_edge = 345
        left_edge = -345

        if y >= top_edge:
            self.up = not self.up

        if x >= right_edge or x <= left_edge:
            self.right = not self.right

        paddle_left_edge = self.paddle.xcor() - 70
        paddle_right_edge = self.paddle.xcor() + 70
        paddle_top_edge = self.paddle.ycor() + 8
        tolerance = 5

        if paddle_left_edge <= x <= paddle_right_edge and paddle_top_edge - tolerance <= y <= paddle_top_edge + tolerance:
            self.up = True

        self.sety(y + self.ball_speed if self.up else y - self.ball_speed)
        self.setx(x + self.ball_speed if self.right else x - self.ball_speed)

        if self.ycor() < self.paddle.ycor() - 50:
            self.sety(0)
            self.setx(0)
            self.increase_speed()
            self.up = False

    def increase_speed(self):
        if self.ball_speed < 10:
            self.ball_speed += 1
