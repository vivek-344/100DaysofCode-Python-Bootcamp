import random
import string
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from flask import Flask, render_template, redirect, url_for, request, session
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
ADMIN = "vivek344@gmail.com"
PASSWORD = "vivek344"


@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        return redirect(url_for('secret'))
    return render_template('login.html', form=form)


@app.route('/secret', methods=['GET'])
def secret():
    auth = session.get('email') == ADMIN and session.get('password') == PASSWORD
    if auth:
        return render_template('success.html')
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
