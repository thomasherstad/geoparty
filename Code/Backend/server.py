from flask import Flask
from flask import render_template

template_dir = '../Frontend/templates'
static_dir = '../Frontend/static'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route("/setup")
def hello_world():
    return render_template('setup.html')

@app.route("/game")
def game():
    return render_template('game.html')