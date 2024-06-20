import turtle
import pandas

s = turtle.Screen()
s.title("U.S. States Game")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    state = s.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if state == "Exit":
        break
    if state in states:
        guessed_states.append(state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state)


missed_states = []
for state in states:
    if state not in guessed_states:
        missed_states.append(state)
data = pandas.DataFrame(missed_states)
data.to_csv("states_to_learn.csv")


s.exitonclick()
