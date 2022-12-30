from random import randint, choice


def show_rules():
    print('What is the result of the expression?')


MIN_OPERAND = 1
MAX_OPERAND = 100


def operand_choice():
    return randint(MIN_OPERAND, MAX_OPERAND)


def operator_choice():
    operator_tuple = ('+', '-', '*')
    return choice(operator_tuple)


def calc_question():
    operator = operator_choice()
    operand_a = operand_choice()
    operand_b = operand_choice()
    if operator == '+':
        correct_answer = operand_a + operand_b
    elif operator == '-':
        correct_answer = operand_a - operand_b
    else:
        correct_answer = operand_a * operand_b
    question = f'{operand_a} {operator} {operand_b}'
    question_tuple = (question, str(correct_answer))
    return question_tuple
