#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print('Answer "yes" if the number is even, otherwise answer "no"')

    def right_answer(num: int) -> str:
        if num % 2 == 0:
            return 'yes'
        return 'no'

    for _ in range(3):
        number = randint(1, 100)
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == right_answer(number):
            print('Correct!')
            continue
        else:
            print("'{}' is wrong answer ;(.".format(answer), end="")
            print(" Correct answer was '{}'.".format(right_answer(number)))
            print("Let's try again, {}".format(name))
            break
    else:
        print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    main()
