import turtle
import pandas as pd

s = turtle.Screen()
s.setup(width=720, height=720)
s.title("Guess Indian States")
image = "map_of_india.gif"
s.addshape(image)
s.bgpic(image)

# def get_click(x, y):
#     print(f",{x},{y}")
#
# s.onscreenclick(get_click)
#
# s.mainloop()

states_data = pd.read_csv("states.csv")
states = states_data.state.to_list()

territories_data = pd.read_csv("union_territories.csv")
territories = territories_data.territory.to_list()

guessed_states = []
guessed_territories = []

while len(guessed_states) + len(guessed_territories) < len(states) + len(territories):
    guess = s.textinput(prompt=f"{len(guessed_states)}/{len(states)} States and "
                               f"{len(guessed_territories)}/{len(territories)} Union Territories Correct",
                        title="Enter a State or a Union Territory").title()

    if guess == "Exit":
        break

    if guess in states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == guess]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        guess = guess.replace(" ", "\n")
        t.write(guess)

    if guess in territories:
        guessed_territories.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        territory_data = territories_data[territories_data.territory == guess]
        t.goto(int(territory_data.x.iloc[0]), int(territory_data.y.iloc[0]))
        guess = guess.replace(" ", "\n")
        t.write(guess)

with open(f"./to_learn", "w") as file:
    file.write("MISSED STATES:\n")

    for state in states:
        if state not in guessed_states:
            file.write(state)
            file.write("\n")

    file.write("\n\nMISSED TERRITORIES:\n")

    for territory in territories:
        if territory not in guessed_territories:
            file.write(territory)
            file.write("\n")

s.exitonclick()
