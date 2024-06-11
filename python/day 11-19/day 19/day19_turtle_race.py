import random
import turtle as t

s = t.Screen()
s.setup(width=720, height=540)

y_pos = -205
colors = ["blue", "red", "purple", "yellow", "orange", "turquoise", "magenta", "cyan"]
mutants = ["Leo", "Raph", "Donnie", "Jenn", "Mikey", "Slash", "Splinter", "Venus"]
turtles = []

bet = t.textinput("Turtle Race", f"Which mutant are you betting on?\nValid Choices are: {mutants}").capitalize()
while bet not in mutants:
    bet = t.textinput("Turtle Race", f"Invalid Input!\nValid Choices are: {mutants}").capitalize()

t.textinput("Turtle Race", f"Your color is {colors[mutants.index(bet)]}. Hit 'OK' to continue.")

for color in colors:
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.turtlesize(1.5)
    turtle.setpos(-320, y_pos)
    turtle.speed("fastest")
    y_pos += 60
    turtles.append(turtle)

x = 0
winner = -1
while x < 310:
    for turtle in turtles:
        move = random.randint(0, 10)
        turtle.fd(move)
        x = turtle.xcor()
        winner = turtles.index(turtle)
        if x >= 310:
            break

if mutants[winner] == bet:
    print(f"Congratulations! The winner is {bet}.")
else:
    print(f"Oops! {bet} lost! The winner is {mutants[winner]}.")

s.exitonclick()
