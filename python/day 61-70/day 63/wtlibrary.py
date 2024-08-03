from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)


def no_cache(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


@app.route('/')
def home():
    all_books = Book.query.all()
    response = make_response(render_template('index.html', books=all_books))
    return no_cache(response)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']
        book = Book(name=name, author=author, rating=rating)
        try:
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('home'))
        except IntegrityError:
            flash('Book title must be unique. A book with this title already exists.', 'error')
    response = make_response(render_template('add.html'))
    return no_cache(response)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
