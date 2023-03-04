from math import sqrt
from random import randint
from brain_games.engine import FIRST_ANSWER, SECOND_ANSWER


QUESTION = (f'Answer "{FIRST_ANSWER}" if given number is prime. '
            f'Otherwise answer "{SECOND_ANSWER}".')

NUMBER_SPREAD = (1, 100)


def is_prime(num: int) -> bool:
    if num in [1, 2]:
        return True
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return False
    return True


def get_answer_and_question() -> tuple:
    number = randint(*NUMBER_SPREAD)
    return is_prime(number), (f"Question: {number}")
