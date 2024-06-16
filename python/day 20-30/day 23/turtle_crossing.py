from turtle_crossing_screen import Display
from turtle_crossing_player import Player
from turtle_crossing_cars import Cars
from turtle_crossing_utilities import Utilities

display = Display()
player = Player()
cars = Cars()
utilities = Utilities()

game_on = True

display.screen.listen()
if game_on:
    display.screen.onkeypress(player.move, "Up")


while game_on:
    display.screen.update()
    cars.create_car()
    cars.move()
    for car in cars.cars:
        if player.distance(car) < 40:
            game_on = False
    if player.ycor() > 320:
        cars.level_up()
        utilities.level_up()
        player.restore()

utilities.game_over()
cars.reset_game()

display.screen.exitonclick()
