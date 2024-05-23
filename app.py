from flask import Flask, redirect, render_template, request, url_for

#TODO: Is the url_for in setup.html form still necessary?

template_dir = './Code/Frontend/templates'
static_dir = './Code/Frontend/static'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('setup'))
    else:
        return render_template('index.html')

@app.route('/setup/', methods =['GET', 'POST'])
def setup():
    if request.method == 'POST':
        data = []
        print(data)
        names = ['team1_name', 'team2_name', 'category1', 'category2', 'category3', 'category4', 'category5', 'xmas-mode']
        for name in names:
            data.append(request.form.get(name))
        return redirect(url_for('game', data = data))
    return render_template('setup.html')

@app.route('/game/', methods =['GET', 'POST'])
def game(data = ['team1_name', 'team2_name', 'category1', 'category2', 'category3', 'category4', 'category5', 'xmas-mode']):
    return render_template('game.html')

