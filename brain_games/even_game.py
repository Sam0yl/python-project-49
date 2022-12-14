from random import randint


def even_question():
    return randint(1, 100000000)


def is_even(number):
    correct_answer = 'no'
    if number % 2 == 0:
        correct_answer = 'yes'
    return correct_answer
