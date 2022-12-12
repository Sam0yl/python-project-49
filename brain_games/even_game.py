import prompt
from random import randint


def even_question():
    return randint(1, 100000000)


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def game(name):
    answers_count = 0
    while answers_count < 3:
        question = even_question()
        check = is_even(question)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if check is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if check is True and answer == 'yes' or check is False and answer == 'no':
            print('Correct!')
            answers_count += 1
        else:
            return print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.\nLet\'s try again, {name}!')
    return print(f'Congratulations, {name}!')
