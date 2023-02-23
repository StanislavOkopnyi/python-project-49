from math import sqrt
from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def right_answer(num: int) -> str:
    if num in [1, 2]:
        return "yes"
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return "no"
    return "yes"


def game() -> str:
    number = randint(1, 100)
    print(f"Question: {number}")
    return right_answer(number)
