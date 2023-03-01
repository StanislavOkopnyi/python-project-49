from random import randint
from brain_games.engine import FIRST_ANSWER, SECOND_ANSWER
from brain_games.bool_to_str import bool_to_str


NUMBER_SPREAD = (1, 100)

QUESTION = (f'Answer "{FIRST_ANSWER}" if the number is even, '
            f'otherwise answer "{SECOND_ANSWER}".')


def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


def get_answer_and_question() -> tuple:
    number = randint(*NUMBER_SPREAD)
    return bool_to_str(is_even(number)), (f'Question: {number}')
