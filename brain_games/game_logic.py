from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user
import prompt


def game(question_func, show_rules):
    greet()
    name = welcome_user()
    show_rules()
    answers_count = 0
    while answers_count < 3:
        question_tuple = question_func()
        correct_answer = question_tuple[1]
        print(f'Question: {question_tuple[0]}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'.',
            )
            return print(f'Let\'s try again, {name}!')
    return print(f'Congratulations, {name}!')
