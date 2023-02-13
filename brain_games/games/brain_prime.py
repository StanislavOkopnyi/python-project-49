#!/usr/bin/env python3
import brain_games.games.templates.conversation_templates as tmp
import prompt
from math import sqrt
from random import randint


def right_answer(num: int) -> str:
    if num in [1, 2]:
        return "yes"
    for div in range(2, int(sqrt(num) + 1)):
        if num % div == 0:
            return "no"
    return "yes"


def main():
    name = tmp.greetings()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        number = randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        if tmp.is_response_correct(user_answer, right_answer(number), name):
            continue
        else:
            break
    else:
        tmp.win(name)


if __name__ == "__main__":
    main()
