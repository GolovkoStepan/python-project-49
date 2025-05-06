from random import randint

TASK_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    number = randint(0, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    return number, correct_answer
