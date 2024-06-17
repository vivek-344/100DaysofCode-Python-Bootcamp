import time
import turtle as t
from snake_logic import Snake
from snake_food import Food
from snake_score import Score

s = t.Screen()
s.setup(width=720, height=640)
s.bgcolor("black")
s.title("Snake Mania")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


def play_game():
    position = True
    while position:
        s.update()
        time.sleep(0.1)
        position = snake.move()

        if snake.head.distance(food) < 10:
            snake.increase_length()
            food.new_food()
            score.points()

        for snakes in snake.snake_body[1:]:
            if snake.head.distance(snakes) < 10 and snake.is_moving:
                position = False

    score.game_over()
    s.update()
    time.sleep(2)
    score.reset()
    snake.reset()
    play_game()


play_game()

s.exitonclick()
