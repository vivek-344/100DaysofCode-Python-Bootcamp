import requests
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    posts = requests.get("https://api.npoint.io/58953a10e49990b48467").json()
    year = datetime.datetime.now().year
    return render_template("index.html", year=year, posts=posts, start=None, end=len(posts)-6)


@app.route('/older_posts')
def older():
    posts = requests.get("https://api.npoint.io/58953a10e49990b48467").json()
    year = datetime.datetime.now().year
    return render_template("index.html", year=year, posts=posts, start=len(posts)-6, end=None)


@app.route("/blog/<int:post_id>")
def blog(post_id):
    posts = requests.get("https://api.npoint.io/58953a10e49990b48467").json()
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return page_not_found(404)  # Call the error handler directly
    return render_template("post.html", year=datetime.datetime.now().year, **post)


@app.route('/about')
def about():
    year = datetime.datetime.now().year
    return render_template("about.html", year=year)


@app.route('/contact')
def contact():
    year = datetime.datetime.now().year
    return render_template("contact.html", year=year)


@app.errorhandler(404)
def page_not_found(error):
    year = datetime.datetime.now().year
    return render_template("404.html", year=year), 404


if __name__ == "__main__":
    app.run(debug=True)
