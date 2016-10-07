import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.urandom(32))
bootstrap = Bootstrap(app)


class UsernameForm(FlaskForm):
    username = TextField('Enter your username:', validators=[Required()])


@app.route('/', methods=['GET', 'POST'])
def index():
    username = None
    form = UsernameForm()
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''
    return render_template('index.html', form=form, username=username)


if __name__ == '__main__':
    app.run(debug=True)

