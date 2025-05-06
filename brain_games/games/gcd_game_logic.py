from math import gcd
from random import randint

TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    correct_answer = str(gcd(number_1, number_2))
    return f'{number_1} {number_2}', correct_answer
