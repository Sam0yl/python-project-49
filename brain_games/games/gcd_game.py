import math
from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


MIN_NUM = 1
MAX_NUM = 100


def number_choice():
    return randint(MIN_NUM, MAX_NUM)


def gcd_question():
    first_number = number_choice()
    second_number = number_choice()
    question = f'{first_number} {second_number}'
    correct_answer = math.gcd(first_number, second_number)
    question_tuple = (question, str(correct_answer))
    return question_tuple
