from random import randint

EVEN_ANSWER = "yes"
OTHERWISE_ANSWER = "no"
NUMBER_SPREAD = (1, 100)

QUESTION = (f'Answer "{EVEN_ANSWER}" if the number is even, '
            f'otherwise answer "{OTHERWISE_ANSWER}".')


def get_right_answer(num: int) -> str:
    if num % 2 == 0:
        return EVEN_ANSWER
    return OTHERWISE_ANSWER


def get_answer_and_question() -> tuple:
    number = randint(*NUMBER_SPREAD)
    return get_right_answer(number), (f'Question: {number}')
