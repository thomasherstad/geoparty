#Game start
#Hent kategorier fra brukeren

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
        self.is_done = False

    def add_points(points_from_question):
        score += points_from_question


class Question():
    def __init__(self, category, points):
        self.category = category
        self.question = ''
        self.answer = ''
        self.points = points
        self.is_active = True
    
    #Asks the AI for a question or gets the question from the database
    def get_question(points):
        pass

    def get_answer():
        pass
    
    def check_answer_given(answer_given):
        pass
    

class Game_board(): 
    def __init__(self, n_categories, n_questions, category_list):
        self.n_categories = n_categories
        self.n_questions = n_questions
        self.category_list = category_list
        self.questions_matrix = self.create_questions()
        self.print_board()
    
    #Returns a matrix with n_categories x n_questions Question objects
    def create_questions(self):
        questions_list = []
        for category in self.category_list:
            category_questions = []
            for i in range(1, self.n_questions+1):
                category_questions.append(Question(category, i*100))
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

def check_if_winner(team1_points, team2_points):
    point_delta = abs(team1_points - team2_points)
    points_left = points_left()
    return points_left < point_delta

if __name__ == '__main__':
    team1 = Team('Lag 1')
    team2 = Team('Lag 2')


    n_categories = 5

    categories = ['Football', 'Geography', 'Nature', 'History', 'Motorsport'] 
    #categories = get_categories(n_categories)
    game_board = Game_board(5, len(categories), categories)

    game_board.print_board()