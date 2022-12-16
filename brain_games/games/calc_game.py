from random import randint, choice


def rules():
    print('What is the result of the exprassion?')


def operand_choice():
    return randint(1, 100)


def operator_choice():
    operator_tuple = ('+', '-', '*')
    return choice(operator_tuple)


def calc_check(string):
    calc_list = string.split()
    if calc_list[1] == '+':
        calc_result = int(calc_list[0]) + int(calc_list[2])
    elif calc_list[1] == '-':
        calc_result = int(calc_list[0]) - int(calc_list[2])
    else:
        calc_result = int(calc_list[0]) * int(calc_list[2])
    return str(calc_result)


def calc_question():
    operator = operator_choice()
    operand_a = str(operand_choice())
    operand_b = str(operand_choice())
    question = f'{operand_a} {operator} {operand_b}'
    correct_answer = calc_check(question)
    question_tuple = (question, correct_answer)
    return question_tuple
