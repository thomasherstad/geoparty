from flask import Flask, redirect, render_template, request, url_for, jsonify
import os
import openai
import json


#TODO: Is the url_for in setup.html form still necessary?

template_dir = './Code/Frontend/templates'
static_dir = './Code/Frontend/static'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

openai.api_key = os.getenv("OPENAI_API_KEY")
chat_model = "gpt-3.5-turbo"

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

def talk(message):
    completion = openai.ChatCompletion.create(
        model = chat_model,
        messages=[
        {"role": "system",
        "content": "You are a cowboy, please talk like one. Keep your response under 50 words."
        },
        {"role": "user", 
        "content": message}
        ]
        )
    return completion.choices[0].message.content

#TODO: FIX TEAM, now it is team 0
@app.route('/question')
def question():
    message = json.loads(request.args.get('message'))
    category = message['category']
    points = message['points']
    try:
        team = message['team']
    except:
        team = None
    try:
        question = message['question']
    except:
        question = None
    try:
        answer = message['answer']
    except:
        answer = None

    print(message)

    if question == None:
        print('question if')
        prompt = f'The category is {category} We need a question worth {points} points'
    elif question != None and answer != None and team != None:
        print('answer if')
        prompt = f'The question was: {question}. Team {team} answered: {answer}. Is that correct?'
    else:
        print('-----Problem in the /question route-----')
        prompt = 'Howdy partner'
    if message:
        print(prompt)
        response = talk(prompt)
    else:
        response = ''
    return jsonify(response)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/ask')
def ask():
    message = request.args.get('message')
    if message:
        print(message)
        response = talk(message)
    else:
        response = ''
    return jsonify(response)

