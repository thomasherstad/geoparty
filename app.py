from flask import Flask, redirect, render_template, request, url_for, jsonify
import os
import openai
import json
from src.backend.tts_controller import *
from src.backend.prompt_handler import get_normal_prompt

#TODO: Is the url_for in setup.html form still necessary?

template_dir = './src/frontend/templates'
static_dir = './src/frontend/static'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

openai.api_key = os.getenv("OPENAI_API_KEY")

gpt_4o = "gpt-4o"
gpt_3_5 = "gpt-3.5-turbo"

chat_model = gpt_4o

SETUP_INFO = {}

use_TTS = False
info_prompt = get_normal_prompt()

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
        global use_TTS, SETUP_INFO
        SETUP_INFO = request.form
        print(SETUP_INFO.get('tts-checkbox'))
        if SETUP_INFO.get('tts-checkbox') == 'on':
            use_TTS = True
        print(f'Text to speech is set to {use_TTS}')
        return render_template('game.html', setup_dict = SETUP_INFO)
    else:
        return render_template('setup.html')

def chat(message):
    completion = openai.ChatCompletion.create(
        model = chat_model,
        messages=[
        {"role": "system",
        "content": info_prompt
        },
        {"role": "user", 
        "content": message}
        ]
        )
    print(f'Text to speech is set to: {use_TTS}, and its type is {type(use_TTS)}')
    if use_TTS == True:
        play_audio(completion.choices[0].message.content)
    return completion.choices[0].message.content

# Need to include where it makes sense
# play_audio(completion.choices[0].message.content)

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
        prompt = f'For {points} points, the question was: {question}. The team {team} answered: {answer}. Is that correct?'
    else:
        print('-----Problem in the /question route-----')
        prompt = 'Howdy partner' #TODO This needs changing
    if message:
        print(prompt)
        response = chat(prompt)
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
        response = chat(message)
    else:
        response = ''
    return jsonify(response)


@app.route('/pass')
def pass_question():
    message = request.args.get('message')
    if message:
        print(message)
        response = chat("Both teams have passed the opportunity to answer. Please shame them and then give us the correct answer")
    else:
        response = ''
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=False)
