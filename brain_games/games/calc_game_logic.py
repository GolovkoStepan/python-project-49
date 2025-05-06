from random import randint

TASK_DESCRIPTION = 'What is the result of the expression?'


def make_question():
    expression = build_expression()
    correct_answer = str(eval(expression))
    return expression, correct_answer


def build_expression():
    number_1 = randint(1, 99)
    number_2 = randint(1, 99)
    sign = ['', '+', '-', '*'][randint(1, 3)]
    return f'{number_1} {sign} {number_2}'
