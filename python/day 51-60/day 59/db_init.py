import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app, model_class=Base)


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

    response = requests.get("https://api.npoint.io/58953a10e49990b48467").json()
    for post in response:
        new_post = BlogPost(
            title=post["title"],
            subtitle=post["subtitle"],
            body=post["body"],
            img_url="https://www.gorecenter.com/wp-content/uploads/2024/07/MIX-Random-dead-women-75-28.jpeg",
            author="Vel",
            date=post["date"]
        )
        db.session.add(new_post)
    db.session.commit()
