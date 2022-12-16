from random import randint


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
    if is_prime(number):
        correct_answer = 'yes'
    correct_answer = 'no'
    return correct_answer


def prime_question():
    question = randint(1, 100)
    correct_answer = check_prime(question)
    question_tuple = (question, correct_answer)
    return question_tuple
