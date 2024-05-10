import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

#TODO: lage en egen prompt til å introdusere quizen
#TODO: Log full quiz conversation

with open("prompt_xmas.txt") as prompt_file:
    prompt = prompt_file.read()

def introduce_quiz():
    pass

def set_category():
    return input('Which category? ')

def set_points():
    return input('How many points? ')

def ask_for_question(prompt, category, points):
    question_prompt = f'Give us a question about {category} worth {points} points'
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
      {"role": "system",
      "content": prompt
      },
      {"role": "user", 
      "content": question_prompt}
      ]
      )
    return completion.choices[0].message.content


def check_answer(answer):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system",
        "content": prompt + '\n' + 'The question was' + question
        },
        {"role": "user", 
        "content": "Is " + answer +"correct?"}
      ]
    )

    return completion.choices[0].message.content


if __name__ == '__main__':
    while True:
        category = set_category()
        points = set_points()
        question = ask_for_question(prompt, category, points)
        print(question)
        answer = input('Answer: ')
        response = check_answer(answer)
        print(response)
        a = input("Continue? ")
        print("--------------------------------------")
        if a == '0':
            break