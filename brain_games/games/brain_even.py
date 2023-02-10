#!/usr/bin/env python3
from random import randint
import prompt
import brain_games.games.templates.conversation_templates as tmp


def main():
    name = tmp.greetings()
    print('Answer "yes" if the number is even, otherwise answer "no"')

    def right_answer(num: int) -> str:
        if num % 2 == 0:
            return 'yes'
        return 'no'

    for _ in range(3):
        number = randint(1, 100)
        print('Question: {}'.format(number))
        user_answer = prompt.string('Your answer: ')

        if tmp.is_response_correct(user_answer, right_answer(number), name):
            continue
        else:
            break
    else:
        tmp.win(name)


if __name__ == "__main__":
    main()
