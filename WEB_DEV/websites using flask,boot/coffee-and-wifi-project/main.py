from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TimeField, URLField
from wtforms.validators import DataRequired, URL
import csv
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY")
Bootstrap5(app)

# Exercise:
# add: Cafe Name, Location URL, open time, closing time, coffee rating, Wi-Fi rating, power outlet rating fields
# make coffee/Wi-Fi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location', validators=[DataRequired(), URL()])
    open = TimeField('Open', validators=[DataRequired()])
    close = TimeField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                        validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=[("0", "✘"), ("1", "💪"), ("2", "💪💪"), ("3", "💪💪💪"), ("4", "💪💪💪💪"), ("5", "💪💪💪💪💪")],
                    validators=[DataRequired()])
    power = SelectField('Power', choices=[("0", "✘"), ("1", "🔌"), ("2", "🔌🔌"), ("3", "🔌🔌🔌"), ("4", "🔌🔌🔌🔌"), ("5", "🔌🔌🔌🔌🔌")],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
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
