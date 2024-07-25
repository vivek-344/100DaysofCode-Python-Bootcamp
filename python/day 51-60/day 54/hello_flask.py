from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, There!"


def make_bold(function):
    def wrapper_function():
        text = function()
        return f"<b>{text}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        text = function()
        return f"<em>{text}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        text = function()
        return f"<u>{text}</u>"

    return wrapper_function


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def goodbye():
    return "Seeya! Have a Nice Day."


if __name__ == "__main__":
    app.run()
