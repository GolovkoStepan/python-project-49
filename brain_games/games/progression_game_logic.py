from random import randint

TASK_DESCRIPTION = 'What number is missing in the progression?'


def make_question():
    numbers_list = generate_list()
    missing_number_index = randint(0, len(numbers_list) - 1)
    missing_number = numbers_list[missing_number_index]
    numbers_list[missing_number_index] = '..'

    return ' '.join(numbers_list), missing_number


def generate_list():
    start = randint(1, 10)
    step = randint(1, 10)
    return [str(x * step + start) for x in range(10)]
