from random import randint
from itertools import product

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_right_answer(num1: int, num2: int) -> str | None:
    num1_divisors = [i for i in range(1, num1 + 1) if num1 % i == 0]
    num2_divisors = [i for i in range(1, num2 + 1) if num2 % i == 0]

    for div1, div2 in product(num1_divisors[::-1], num2_divisors):
        if div1 == div2:
            return str(div1)


def get_answer_and_question() -> tuple:
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    return (get_right_answer(number1, number2),
            (f'Question: {number1} {number2}'))
