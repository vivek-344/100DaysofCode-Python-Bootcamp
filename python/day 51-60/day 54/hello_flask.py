from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, There!"


@app.route("/bye")
def goodbye():
    return "Seeya! Have a Nice Day."


if __name__ == "__main__":
    app.run()
