from flask import Flask, render_template, request
from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class RegisForm(FlaskForm):
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired(), Length(min=8, message="Password at least 8 characters!")])
    name = StringField("name", validators=[InputRequired()])
    last = StringField("last", validators=[InputRequired()])
    email = StringField("Email",  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])


@app.route('/')
def student():
    form = RegisForm()
    return render_template('index.html', form=form)


@app.route('/regis', methods=["GET", "POST"])
def regis():
    form = RegisForm()
    if form.validate_on_submit():
        return "The form has been submitted"
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
