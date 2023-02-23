from random import randint

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def right_answer(num: int) -> str:
    if num % 2 == 0:
        return "yes"
    return "no"


def game() -> str:
    number = randint(1, 100)
    print('Question: {}'.format(number))
    return right_answer(number)
