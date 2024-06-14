from pong_screen import Display
from pong_paddle import Paddle

display = Display()
paddle = Paddle()

key_mappings = ["w", "s", "Up", "Down"]

display.screen.listen()
for key in key_mappings:
    display.screen.onkeypress(lambda d=key: paddle.handle_keypress(d), key)
    display.screen.onkeyrelease(lambda d=key: paddle.handle_keyrelease(d), key)

while True:
    paddle.update_paddles()
    display.update_screen()
