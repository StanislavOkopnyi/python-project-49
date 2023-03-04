from random import randint, choice

QUESTION = "What is the result of the expression?"

NUMBER_SPREAD = (1, 30)

OPERATORS = ['+', '-', '*']


def get_right_answer(num1: int, num2: int, operator: str) -> int | None:
    if operator == "*":
        return num1 * num2
    elif operator == "-":
        return num1 - num2
    elif operator == "+":
        return num1 + num2


def get_answer_and_question() -> tuple:
    operand1 = (randint(*NUMBER_SPREAD))
    operand2 = (randint(*NUMBER_SPREAD))
    operator = choice(OPERATORS)

    return (get_right_answer(operand1, operand2, operator),
            (f'Question: {operand1} {operator} {operand2}'))
