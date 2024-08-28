from screen import Display
from bricks import Bricks
from paddle import Paddle
from turtle import Turtle
from ball import Ball

bricks = Bricks()
display = Display()
paddle = Paddle()
ball = Ball(paddle.paddle, bricks.bricks)

paddle.assign_ball(ball)
bricks.assign_ball(ball)

key_mappings = ["Left", "Right"]

display.screen.listen()
for key in key_mappings:
    display.screen.onkeypress(lambda d=key: paddle.handle_keypress(d), key)
    display.screen.onkeyrelease(lambda d=key: paddle.handle_keyrelease(d), key)

while True:
    display.update_screen()
    if len(bricks.bricks) > 0:
        paddle.update_paddles()
        ball.move()
    else:
        ball.hideturtle()
        t = Turtle()
        t.hideturtle()
        t.color("white")
        t.penup()
        t.goto(0, 0)
        t.write(arg="YOU WIN!", align="center", font=("Courier", 18, "bold"))
