from random import randint


def rules():
    print('What number is missing in the progression?')


def create_progression():
    number = randint(1, 50)
    initial_term = randint(1, 10)
    progression_list = []
    list_length = 10
    while list_length > 0:
        progression_list.append(str(number))
        number += initial_term
        list_length -= 1
    return progression_list


def progression_question():
    progression_list = create_progression()
    element = randint(0, 9)
    correct_answer = progression_list[element]
    progression_list[element] = '..'
    question = " ".join(progression_list)
    question_tuple = (question, correct_answer)
    return question_tuple
