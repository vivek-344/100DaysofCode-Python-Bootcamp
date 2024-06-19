import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state name?").title()

    if state in states:
        guessed_state.append(state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state)

screen.exitonclick()
