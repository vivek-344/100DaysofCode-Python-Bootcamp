import time
import turtle as t

from snake_logic import Snake

s = t.Screen()
s.setup(width=720, height=640)
s.bgcolor("black")
s.title("Snake Mania")
s.tracer(0)

snake = Snake()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

position = True
while position:
    s.update()
    time.sleep(0.1)
    position = snake.move()


s.exitonclick()
