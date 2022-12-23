from random import randint


def show_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def check_even(number):
    correct_answer = 'no'
    if number % 2 == 0:
        correct_answer = 'yes'
    return correct_answer


MIN_NUM = 1
MAX_NUM = 100


def even_question():
    question = randint(MIN_NUM, MAX_NUM)
    correct_answer = check_even(question)
    question_tuple = (question, correct_answer)
    return question_tuple
