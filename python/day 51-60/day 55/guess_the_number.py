import random
from flask import Flask

app = Flask(__name__)

NUM = None


@app.route('/')
def home():
    rand()
    return ("<h1 style='color: blue;'>You can guess!</h1>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjN5NWV5NDQ2YjJueGM0OWhoNXZkNjBlanFkdGt5N2d1d3E0dn"
            "J0dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2vmfW3evTraeJEcoAv/giphy.gif' width=480>")


def rand():
    global NUM
    NUM = random.randint(0, 9)


@app.route('/<int:guess>')
def check(guess):
    global NUM
    if guess < NUM:
        return ("<h1 style='color: red;'>Too low!</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWxseWk1d2M4bG11YnFtdHFhM3J2a3JlcDMzNWs0c3p4azN"
                "0ZTU0YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif' width=480>")
    elif guess > NUM:
        return ("<h1 style='color: red;'>Too high!</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJkM3FwZG5oYnAwZm5ibWFnOXhuYW9iZWk4N3NpbGN"
                "vczlvYzNqOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KpAPQVW9lWnWU/giphy.gif' width=480>")
    else:
        rand()
        return ("<h1 style='color: green;'>You Win! Guess Again?</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmZsOHhteWZxdnVxMDJ2aWg5OXd0Y2loc241YmI4OWlxZG"
                "xra3h4OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEjHV0z8S7WM4MwnK/giphy.gif' width=480>")


if __name__ == "__main__":
    app.run(debug=True)
