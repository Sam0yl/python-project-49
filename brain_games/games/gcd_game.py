import math
from random import randint


def number_choice():
    return randint(1, 100)


def gcd_question():
    first_number = str(number_choice())
    second_number = str(number_choice())
    return f'{first_number} {second_number}'


def gcd_check(string):
    numbers_list = string.split()
    gcd = math.gcd(int(numbers_list[0]), int(numbers_list[1]))
    return str(gcd)
