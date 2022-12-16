from random import randint


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def check_even(number):
    correct_answer = 'no'
    if number % 2 == 0:
        correct_answer = 'yes'
    return correct_answer


def even_question():
    question = randint(1, 100)
    correct_answer = check_even(question)
    question_tuple = (question, correct_answer)
    return question_tuple
