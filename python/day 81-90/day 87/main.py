from screen import Display
from paddle import Paddle
from ball import Ball

display = Display()
paddle = Paddle()
ball = Ball(paddle.paddle)

paddle.assign_ball(ball)

key_mappings = ["Left", "Right"]

display.screen.listen()
for key in key_mappings:
    display.screen.onkeypress(lambda d=key: paddle.handle_keypress(d), key)
    display.screen.onkeyrelease(lambda d=key: paddle.handle_keyrelease(d), key)

while True:
    paddle.update_paddles()
    display.update_screen()
    ball.move()
