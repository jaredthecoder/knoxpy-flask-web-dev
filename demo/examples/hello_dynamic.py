from flask import Flask


app = Flask(__name__)


@app.route('/message/<uuid>')
def message(uuid):
    return 'Message with ID: <b>{}</b>'.format(uuid)


@app.route('/home/<name>')
def home(name):
    return "Welcome Home, <i>{}</i>".format(name)


if __name__ == '__main__':
    app.run(debug=True)
