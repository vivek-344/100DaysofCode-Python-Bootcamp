import os
import requests
import datetime
import smtplib
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

load_dotenv()
app = Flask(__name__)


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


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
        return page_not_found(404)
    return render_template("post.html", year=datetime.datetime.now().year, **post)


@app.route('/about')
def about():
    year = datetime.datetime.now().year
    return render_template("about.html", year=year)


@app.route('/contact')
def contact():
    year = datetime.datetime.now().year
    return render_template("contact.html", year=year)


@app.route('/send_mail', methods=["POST"])
def send_mail():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("No data received")

        if request.method == 'POST':
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(
                    EMAIL,
                    EMAIL,
                    msg=f"Subject: New Contact Form Submission\n\n"
                        f"Name: {data['name']}\n"
                        f"Email: {data['email']}\n"
                        f"Phone: {data['phone']}\n"
                        f"Message: {data['message']}"
                )

        return jsonify({"message": "Form submission successful!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Error processing the form submission."}), 500


@app.errorhandler(404)
def page_not_found(error):
    year = datetime.datetime.now().year
    return render_template("404.html", year=year), 404


if __name__ == "__main__":
    app.run(debug=True)
