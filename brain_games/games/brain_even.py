from random import randint
from brain_games.engine import FIRST_ANSWER, SECOND_ANSWER

NUMBER_SPREAD = (1, 100)

QUESTION = (f'Answer "{FIRST_ANSWER}" if the number is even, '
            f'otherwise answer "{SECOND_ANSWER}".')


def get_right_answer(num: int) -> str:
    if num % 2 == 0:
        return FIRST_ANSWER
    return SECOND_ANSWER


def get_answer_and_question() -> tuple:
    number = randint(*NUMBER_SPREAD)
    return get_right_answer(number), (f'Question: {number}')
