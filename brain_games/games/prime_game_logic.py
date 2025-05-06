from random import randint

TASK_DESCRIPTION = 'Answer "yes" if given number is prime.' \
                   ' Otherwise answer "no".'


def make_question():
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def is_prime(n):  
    if n <= 1:  
        return False 
    if n == 2:  
        return True 
    if n % 2 == 0:  
        return False 
    for i in range(3, int(n ** 0.5) + 1, 2):  
        if n % i == 0:  
            return False 
    return True 
