import csv

questions_csv = []
answers_csv = []

with open('/Users/Thomas/Documents/Geoparty/Code/Backend/questions_answers.csv', newline='') as csvfile:
    questions_bank = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in questions_bank:
        questions_csv.append(row[0])
        answers_csv.append(row[1])


print(questions_csv[10])
print(answers_csv[10])