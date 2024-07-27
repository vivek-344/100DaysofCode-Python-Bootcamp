import requests
import datetime as dt
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    year = dt.datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    country = requests.get(f"https://api.nationalize.io?name={name}").json()["country"][0]["country_id"]
    return render_template("guess.html", name=name.title(), age=age, gender=gender, country=country)


if __name__ == "__main__":
    app.run(debug=True)
