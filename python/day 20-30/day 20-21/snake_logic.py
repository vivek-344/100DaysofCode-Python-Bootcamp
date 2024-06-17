import turtle as t

INITIAL_POSITIONS = [(40, 0), (20, 0), (0, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake()
        self.head = self.snake_body[0]
        self.is_moving = False  # New attribute to track if the snake is moving

    def snake(self):
        for movement in INITIAL_POSITIONS:
            self.add_snake_object(movement)

    def add_snake_object(self, movement):
        turtle = t.Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.setpos(movement)
        self.snake_body.append(turtle)

    def increase_length(self):
        self.add_snake_object(self.snake_body[-1].position())

    def move(self):
        if not self.is_moving:  # Check if the snake should move
            return True
        for snake in range(len(self.snake_body) - 1, 0, -1):
            pos = self.snake_body[snake - 1].pos()
            self.snake_body[snake].goto(pos)
        self.head.fd(MOVE_DISTANCE)
        if -360 < self.head.xcor() < 360 and -320 < self.head.ycor() < 320:
            return True
        return False

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.is_moving = True  # Start moving the snake

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.is_moving = True  # Start moving the snake

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.is_moving = True  # Start moving the snake

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.is_moving = True  # Start moving the snake

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)  # Move the segments off-screen
        self.snake_body.clear()  # Clear the snake body list
        self.snake()  # Create the initial snake again
        self.head = self.snake_body[0]
        self.is_moving = False  # Reset the movement state
