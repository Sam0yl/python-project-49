from random import randint


def show_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


MIN_NUM = 1
MAX_NUM = 100


def prime_question():
    question = randint(MIN_NUM, MAX_NUM)
    correct_answer = 'no'
    if is_prime(question):
        correct_answer = 'yes'
    question_tuple = (question, correct_answer)
    return question_tuple
