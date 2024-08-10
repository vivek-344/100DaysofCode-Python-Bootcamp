import os
import datetime
from dotenv import load_dotenv
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField
import smtplib


load_dotenv()
app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = 'SOME_KEY'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


class BlogForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Blog Post Subtitle', validators=[DataRequired()])
    name = StringField("Your Name", validators=[DataRequired()])
    url = URLField("Image URL", validators=[DataRequired()])
    content = CKEditorField('Blog Content')
    submit = SubmitField("Submit")


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/home')
def home():
    posts = BlogPost.query.all()
    year = datetime.datetime.now().year
    return render_template("index.html", year=year, posts=posts, start=None, end=len(posts)-6)


@app.route('/older_posts')
def older():
    posts = BlogPost.query.all()
    year = datetime.datetime.now().year
    return render_template("index.html", year=year, posts=posts, start=len(posts)-6, end=None)


@app.route("/blog/<int:post_id>")
def blog(post_id):
    post = BlogPost.query.get(post_id)
    if not post:
        return page_not_found(404)
    return render_template("post.html", year=datetime.datetime.now().year, post=post)


@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    form = BlogForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.content.data,
            img_url=form.url.data,
            author=form.name.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("make-post.html", form=form, action="Add new Post")


@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    form = BlogForm(
        title=post.title,
        subtitle=post.subtitle,
        name=post.author,
        url=post.img_url,
        content=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.content.data
        post.img_url = form.url.data
        post.author = form.name.data
        post.date = date.today().strftime("%B %d, %Y")
        db.session.commit()
        return redirect(url_for("blog", post_id=post_id))
    return render_template("make-post.html", form=form, action="Edit Post")


@app.route('/delete-post/<post_id>', methods=['GET', 'DELETE'])
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))


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
