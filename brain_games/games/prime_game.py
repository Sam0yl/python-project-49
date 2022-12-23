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


def check_prime(number):
    correct_answer = 'no'
    if is_prime(number):
        correct_answer = 'yes'
    return correct_answer


MIN_NUM = 1
MAX_NUM = 100


def prime_question():
    question = randint(MIN_NUM, MAX_NUM)
    correct_answer = check_prime(question)
    question_tuple = (question, correct_answer)
    return question_tuple
