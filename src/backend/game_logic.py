#Game start
#Hent kategorier fra brukeren
import os #for front end

def get_categories(number_of_categories):
    categories = []
    for i in range(number_of_categories):
        categories.append(input(f'What is category number {i+1}: '))
    return categories

def print_categories(categories):
    print(f'Okay, so your categories for the game are', end=' ')
    for category in categories:
        if category is not categories[-1]:
            print(f'{category.lower()},', end = ' ')
        elif category is categories[-1]:
            print(f'and {category.lower()}.')

def confirm_game_start(categories):
    print_categories(categories)
    ans = input('Would you like to start the game? y/n \n')
    if ans.lower() == 'y':
        return 1
    elif ans.lower() == 'n':
        return 0
    else:
        print('Could not recognize answer. Retrying...')
        return confirm_game_start(categories)

def create_categories(n_categories):
    categories = []
    for i in range(n_categories):
        categories[i] = input(f'Category {i+1}: ')



# Håndtering av lagene
class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.is_winner = False
        self.is_done = False #Hva er denne til igjen?

    def award_points(self, points_from_question):
        self.score += points_from_question
        print(f'Awarded {points_from_question} to {self.name}')


class Question():
    def __init__(self, category, points):
        self.category = category
        self.question = 'Q ' + category + ' ' + str(points)
        self.answer = 'A ' + category + ' ' + str(points)
        self.points = points
        self.is_active = True
    
    #Asks the AI for a question or gets the question from the database

    def populate_question_from_bank(self, q_list, a_list, n):
        self.question = q_list[n]
        self.answer = a_list[n]

    def get_question_from_LLM(points):
        pass
    
    def check_answer_given(self,answer_given):
        if answer_given.lower() == self.answer.lower():
            return 1
        else:
            return 0
    
    def print_question(self):
        print(self.question)

    def print_answer(self):
        print(f'The correct answer is {self.answer}')


class Game_board(): 
    def __init__(self, n_questions, category_list):
        self.n_categories = len(category_list)
        self.n_questions = n_questions
        self.category_list = category_list
        self.llm_mode = False
        self.questions_matrix = self.create_questions()
        
    
    #Returns a matrix with n_categories x n_questions Question objects
    def create_questions(self):
        questions_list = []
        for category in self.category_list:
            category_questions = []
            for i in range(1, self.n_questions+1):
                category_questions.append(Question(category, i*100))
                #category_questions[category][i]
            questions_list.append(category_questions)
        return questions_list

    #Not needed for actual build, but nice for debug atm
    def print_board(self):
        for category in self.category_list:
            print(category, end = '\t')
        print()
        for i in range(len(self.questions_matrix)):
            for j in range(len(self.questions_matrix[i])):
                if self.questions_matrix[j][i].is_active:
                    print(f'{self.questions_matrix[j][i].points}{self.questions_matrix[j][i].category[0]}', end ='\t')
                else:
                    print('----', end = '\t')
            print()

    def points_left(self):
        sum = 0
        for questions_list in self.questions_matrix:
            for question in questions_list:
                if question.is_active == True:
                    sum += int(question.points)
        return sum
    

# Håndtering av poeng

def check_if_winner(team1_points, team2_points, points_left):
    point_delta = abs(team1_points - team2_points)
    return points_left < point_delta

if __name__ == '__main__':
    team1 = Team('Lag 1')
    team2 = Team('Lag 2')
    teams = [team1, team2]


    n_categories = 5

    categories = ['Football', 'Geography', 'Nature', 'History', 'Motorsport']
    #categories = get_categories(n_categories)
    game_board = Game_board(5, categories)
    play = '1'
    
    while(play == '1'):
        os.system('clear')
        game_board.print_board()
        
        chosen_category = int(input('Hvilken kategori? '))
        chosen_value = int(input('Hvilken verdi? '))
        active_question = game_board.questions_matrix[chosen_category][chosen_value]
        print(f'Du har valgt kategori {active_question.category} med verdi {active_question.points}')

        active_question.print_question()

        active_team = teams[int(input('Hvilket lag skal svare? '))]

        active_question.print_answer()
        correct = int(input('Svarte laget korrekt? '))
        if correct == True:
            active_team.award_points(active_question.points)
            active_question.is_active = False

        print(f'Det står {teams[0].score} - {teams[1].score}')

        print(f'Det er {game_board.points_left()} poeng igjen på brettet.')
        if check_if_winner(teams[0].score, teams[1].score, game_board.points_left()) == True:
            if teams[0].score > teams[1].score:
                print(f'{teams[0].name} har vunnet!')
            elif teams[0].score < teams[1].score:
                print(f'{teams[1].name} har vunnet!')
            play = 0
        else:
            play = input('Fortsette? 0/1 ')
