from random import randint, choice

QUESTION = "What is the result of the expression?"


def get_right_answer(num1: int, num2: int, operator: str) -> str | None:
    if operator == "*":
        return str(num1 * num2)
    elif operator == "-":
        return str(num1 - num2)
    elif operator == "+":
        return str(num1 + num2)


def get_answer_and_question() -> tuple:
    operand1 = (randint(1, 30))
    operand2 = (randint(1, 30))
    operator = choice(['+', '-', '*'])

    return (get_right_answer(operand1, operand2, operator),
            (f'Question: {operand1} {operator} {operand2}'))
