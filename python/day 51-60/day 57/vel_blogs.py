import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", posts=posts, id=post_id)


if __name__ == "__main__" :
    app.run(debug=True)
