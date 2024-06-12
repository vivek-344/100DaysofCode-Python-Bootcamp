import turtle as t

INITIAL_MOVEMENTS = [0, 20, 40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake()
        self.head = self.snake_body[0]

    def snake(self):
        for movement in INITIAL_MOVEMENTS:
            turtle = t.Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.bk(movement)
            self.snake_body.append(turtle)

    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            pos = self.snake_body[snake - 1].pos()
            self.snake_body[snake].goto(pos)
        self.head.fd(MOVE_DISTANCE)
        if -360 <= self.head.xcor() <= 360 and -320 <= self.head.ycor() <= 320:
            return True
        return False

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
