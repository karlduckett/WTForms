from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf


app = Flask(__name__)
app.config['SECRET_KEY'] = 'suffertheslingsandarrows'


#Flask form adds a CRFS token by default (wtform doesnt)
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=25, message='Must be between 3 and 25')])
    password = PasswordField('password', validators=[InputRequired(Length(min=6, max=25, message='Must be between 6 and 25'))])

#Could separate the GET/POST but with one form it easier to keep them together...
@app.route('/', methods=['GET','POST']) 
def index():
    form = LoginForm()
    # form.validate_on_submit happens on req -- also check CRFS token here
    if form.validate_on_submit():
        return '<h1>Username: {} Password {} </h1>'.format(form.username.data, form.password.data)

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

