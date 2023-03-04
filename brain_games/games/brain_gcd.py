from random import randint
from itertools import product

QUESTION = 'Find the greatest common divisor of given numbers.'

NUMBER_SPREAD = (1, 100)


def get_right_answer(num1: int, num2: int) -> int | None:
    num1_divisors = [i for i in range(1, num1 + 1) if num1 % i == 0]
    num2_divisors = [i for i in range(1, num2 + 1) if num2 % i == 0]

    for div1, div2 in product(num1_divisors[::-1], num2_divisors):
        if div1 == div2:
            return div1


def get_answer_and_question() -> tuple:
    number1 = randint(*NUMBER_SPREAD)
    number2 = randint(*NUMBER_SPREAD)
    return (get_right_answer(number1, number2),
            (f'Question: {number1} {number2}'))
