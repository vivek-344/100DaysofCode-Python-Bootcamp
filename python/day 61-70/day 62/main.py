import os
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, URLField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location URL', validators=[DataRequired()])
    open_time = TimeField("Open Time", validators=[DataRequired()])
    close_time = TimeField("Close Time", validators=[DataRequired()])
    coffee = SelectField('Coffee Rating',
                         choices=[('☕️', '☕️'),
                                  ('☕️☕️', '☕️☕️'),
                                  ('☕️☕️☕️', '☕️☕️☕️'),
                                  ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                  ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')],
                         validators=[DataRequired()])
    wifi = SelectField('Wifi Rating',
                       choices=[('✘', '✘'),
                                ('🛜', '🛜'),
                                ('🛜🛜', '🛜🛜'),
                                ('🛜🛜🛜', '🛜🛜🛜'),
                                ('🛜🛜🛜🛜', '🛜🛜🛜🛜'),
                                ('🛜🛜🛜🛜🛜', '🛜🛜🛜🛜🛜')],
                       validators=[DataRequired()])
    power_outlet = SelectField('Coffee Rating',
                               choices=[('✘', '✘'),
                                        ('🔌', '🔌'),
                                        ('🔌🔌', '🔌🔌'),
                                        ('🔌🔌🔌', '🔌🔌🔌'),
                                        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                        ('🔌🔌🔌🔌🔌', '🔌🔌️🔌🔌🔌')],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        file_path = 'cafe-data.csv'
        file_exists = os.path.isfile(file_path)
        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Cafe Name', 'Location', 'Open', 'Close', 'Coffee', 'Wifi', 'Power']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            cafe = form.cafe.data
            location = form.location.data
            open_time = form.open_time.data
            close_time = form.close_time.data
            coffee = form.coffee.data
            wifi = form.wifi.data
            power_outlet = form.power_outlet.data

            if not file_exists:
                writer.writeheader()

            writer.writerow({'Cafe Name': cafe,
                             'Location': location,
                             'Open': open_time,
                             'Close': close_time,
                             'Coffee': coffee,
                             'Wifi': wifi,
                             'Power': power_outlet})
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
