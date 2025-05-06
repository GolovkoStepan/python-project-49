import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def task_message(task):
    print(task)


def question_message(question):
    print(f'Question: {question}')


def get_user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def correct_answer_message():
    print('Correct!')


def wrong_answer_message(user_name, user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(.", 
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")


def congratulation_message(user_name):
    print(f'Congratulations, {user_name}!')
