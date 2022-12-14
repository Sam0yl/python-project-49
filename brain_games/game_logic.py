import prompt


def text_of_losing(answer, correct_answer, name):
    print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.\nLet\'s try again, {name}!')


def text_of_wining(name):
    print(f'Congratulations, {name}!')


def ask_answer():
    answer = prompt.string('Your answer: ')
    return answer


def game(question_func, check_func, name):
    answers_count = 0
    while answers_count < 3:
        question = question_func()
        correct_answer = check_func(question)
        print(f'Question: {question}')
        answer = ask_answer()
        if answer == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            return text_of_losing(answer, correct_answer, name)
    return text_of_wining(name)
