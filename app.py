from flask import Flask, redirect, render_template, request, url_for

#TODO: Is the url_for in setup.html form still necessary?

template_dir = './Code/Frontend/templates'
static_dir = './Code/Frontend/static'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

SETUP_INFO = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('setup'))
    else:
        return render_template('index.html')

@app.route('/setup', methods =['GET', 'POST'])
def setup():
    if request.method == 'POST':
        return redirect(url_for('game'))
    return render_template('setup.html')

@app.route('/game', methods =['GET', 'POST'])
def game():
    if request.method == 'POST':
        SETUP_INFO = request.form
        return render_template('game.html', setup_dict = SETUP_INFO)
    else:
        return render_template('setup.html')

