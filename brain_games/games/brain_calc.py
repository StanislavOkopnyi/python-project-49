from random import randint, choice

QUESTION = "What is the result of the expression?"

NUMBER_SPREAD = (1, 30)

OPERATORS = ['+', '-', '*']


def get_right_answer(num1: int, num2: int, operator: str) -> str | None:
    if operator == "*":
        return str(num1 * num2)
    elif operator == "-":
        return str(num1 - num2)
    elif operator == "+":
        return str(num1 + num2)


def get_answer_and_question() -> tuple:
    operand1 = (randint(*NUMBER_SPREAD))
    operand2 = (randint(*NUMBER_SPREAD))
    operator = choice(OPERATORS)
    right_answer = get_right_answer(operand1, operand2, operator)
    task = f'Question: {operand1} {operator} {operand2}'

    return right_answer, task
