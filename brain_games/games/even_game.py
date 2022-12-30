from random import randint


def show_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    if number % 2 == 0:
        return True
    return False


MIN_NUM = 1
MAX_NUM = 100


def even_question():
    question = randint(MIN_NUM, MAX_NUM)
    correct_answer = 'no'
    if is_even(question):
        correct_answer = 'yes'
    question_tuple = (question, correct_answer)
    return question_tuple
