from math import sqrt
from random import randint
from brain_games.engine import FIRST_ANSWER, SECOND_ANSWER


QUESTION = (f'Answer "{FIRST_ANSWER}" if given number is prime. '
            f'Otherwise answer "{SECOND_ANSWER}".')


def get_right_answer(num: int) -> str:
    if num in [1, 2]:
        return FIRST_ANSWER
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return SECOND_ANSWER
    return FIRST_ANSWER


def get_answer_and_question() -> tuple:
    number = randint(1, 100)
    return get_right_answer(number), (f"Question: {number}")
