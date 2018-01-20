from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'ThisIsNotMuchOfASecret'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(message='A username is required.'),])
    password = PasswordField('password', validators=[InputRequired(message='A password is required.'),])

@app.route('/')
def index():
    return "here"

@app.route('/form', methods=['GET','POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        # I didn't need to check the request route since validate_on_submit does that itself
        # normally, you would get the input fields from the request object
        # username = request.form.get('username') or password = request.form.get('password')
        return 'Form submitted with values username={} password={}'.format(form.username.data, form.password.data)
            
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=False)