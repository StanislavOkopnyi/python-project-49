import brain_games.games.templates.conversation_templates as tmp
from random import randint
from itertools import product
import prompt


def main():
    name = tmp.greetings()
    print('Find the greatest common divisor of given numbers.')

    def right_answer(num1: int, num2: int) -> str:
        num1_divisors = [i for i in range(1, num1 + 1) if num1 % i == 0]
        num2_divisors = [i for i in range(1, num2 + 1) if num2 % i == 0]

        for div1, div2 in product(num1_divisors[::-1], num2_divisors):
            if div1 == div2:
                return str(div1)

    for _ in range(3):
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        print('Question: {}, {}'.format(number1, number2))
        user_answer = prompt.string('Your answer: ')

        if tmp.is_response_correct(user_answer,
                                   right_answer(number1, number2), name):
            continue
        else:
            break
    else:
        tmp.win(name)


if __name__ == "__main__":
    main()
