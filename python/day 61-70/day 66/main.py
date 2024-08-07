# doc: https://documenter.getpostman.com/view/36792613/2sA3rzKY4f

import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)
KEY = "VIVEK"


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.as_dict()), 200


@app.route("/all", methods=["GET"])
def get_all_cafe():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.as_dict() for cafe in all_cafes]), 200


@app.route("/search", methods=["GET"])
def get_cafe():
    location = request.args.get("location")
    if location:
        all_cafes = Cafe.query.filter(Cafe.location == location).all()
        if all_cafes:
            return jsonify(cafes=[cafe.as_dict() for cafe in all_cafes]), 200
        else:
            error_dict = {"error": "Sorry! We don't serve at that location."}
            return jsonify(error_dict), 404
    else:
        error_dict = {"error": "Location arg missing!"}
        return jsonify(error_dict), 404


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    price = request.args.get("price")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        if price:
            cafe.coffee_price = price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the cafe."}), 200
        else:
            error_dict = {"error": "Price arg missing!"}
            return jsonify(error_dict), 404
    else:
        error_dict = {"error": "Cafe not found!"}
        return jsonify(error_dict), 404


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    key = request.args.get("API_KEY")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        if key == KEY:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            error_dict = {"error": "API Key missing!"}
            return jsonify(error_dict), 403
    else:
        error_dict = {"error": "Cafe not found!"}
        return jsonify(error_dict), 404


if __name__ == '__main__':
    app.run(debug=True)
