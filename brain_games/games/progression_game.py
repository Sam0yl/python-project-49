from random import randint


RULES = 'What number is missing in the progression?'


MIN_NUM = 1
MAX_NUM = 50


def random_first_number_of_progression():
    return randint(MIN_NUM, MAX_NUM)


MIN_STEP = 1
MAX_STEP = 10


def random_step_of_progression():
    return randint(MIN_STEP, MAX_STEP)


PROGRESSION_LENGTH = 10


def create_progression():
    number = random_first_number_of_progression()
    step_of_progression = random_step_of_progression()
    progression_list = []
    list_length = PROGRESSION_LENGTH
    while list_length > 0:
        progression_list.append(str(number))
        number += step_of_progression
        list_length -= 1
    return progression_list


MIN_ELEMENT = 0
MAX_ELEMENT = 9


def random_element_of_progression():
    return randint(MIN_ELEMENT, MAX_ELEMENT)


def progression_question():
    progression_list = create_progression()
    element_of_progression = random_element_of_progression()
    correct_answer = progression_list[element_of_progression]
    progression_list[element_of_progression] = '..'
    question = " ".join(progression_list)
    question_tuple = (question, correct_answer)
    return question_tuple
