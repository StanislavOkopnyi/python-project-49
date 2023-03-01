from math import sqrt
from random import randint
from brain_games.engine import FIRST_ANSWER, SECOND_ANSWER
from brain_games.bool_to_str import bool_to_str


QUESTION = (f'Answer "{FIRST_ANSWER}" if given number is prime. '
            f'Otherwise answer "{SECOND_ANSWER}".')


def is_prime(num: int) -> bool:
    if num in [1, 2]:
        return True
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return False
    return True


def get_answer_and_question() -> tuple:
    number = randint(1, 100)
    return bool_to_str(is_prime(number)), (f"Question: {number}")
