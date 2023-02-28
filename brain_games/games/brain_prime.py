from math import sqrt
from random import randint


PRIME_ANSWER = "yes"
OTHERWISE_ANSWER = "no"


QUESTION = (f'Answer "{PRIME_ANSWER}" if given number is prime. '
            f'Otherwise answer "{OTHERWISE_ANSWER}".')


def get_right_answer(num: int) -> str:
    if num in [1, 2]:
        return PRIME_ANSWER
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return OTHERWISE_ANSWER
    return PRIME_ANSWER


def get_answer_and_question() -> tuple:
    number = randint(1, 100)
    return get_right_answer(number), (f"Question: {number}")
