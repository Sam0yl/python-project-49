from random import randint, choice


RULES = 'What is the result of the expression?'


MIN_OPERAND = 1
MAX_OPERAND = 100


def operand_choice():
    return randint(MIN_OPERAND, MAX_OPERAND)


def operator_choice():
    operator_tuple = ('+', '-', '*')
    return choice(operator_tuple)


def calc_correct_answer(num1, num2, operation):
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return correct_answer


def calc_question():
    operator = operator_choice()
    operand_a = operand_choice()
    operand_b = operand_choice()
    correct_answer = calc_correct_answer(operand_a, operand_b, operator)
    question = f'{operand_a} {operator} {operand_b}'
    question_tuple = (question, str(correct_answer))
    return question_tuple
