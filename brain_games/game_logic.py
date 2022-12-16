import prompt


def text_of_losing(answer, real_answer, name):
    print(f''''{answer}' is wrong answer ;(. Correct answer was '{real_answer}'.
Let's try again, {name}!''')


def text_of_wining(name):
    print(f'Congratulations, {name}!')


def ask_answer():
    answer = prompt.string('Your answer: ')
    return answer


def game(question_func, name):
    answers_count = 0
    while answers_count < 3:
        question_tuple = question_func()
        correct_answer = question_tuple[1]
        print(f'Question: {question_tuple[0]}')
        answer = ask_answer()
        if answer == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            return text_of_losing(answer, correct_answer, name)
    return text_of_wining(name)
