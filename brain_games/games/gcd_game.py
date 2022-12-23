import math
from random import randint


def show_rules():
    print('Find the greatest common divisor of given numbers.')


MIN_NUM = 1
MAX_NUM = 100


def number_choice():
    return randint(MIN_NUM, MAX_NUM)


def gcd_check(string):
    numbers_list = string.split()
    gcd = math.gcd(int(numbers_list[0]), int(numbers_list[1]))
    return str(gcd)


def gcd_question():
    first_number = str(number_choice())
    second_number = str(number_choice())
    question = f'{first_number} {second_number}'
    correct_answer = gcd_check(question)
    question_tuple = (question, correct_answer)
    return question_tuple
