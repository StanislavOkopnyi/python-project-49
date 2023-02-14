import brain_games.games.templates.conversation_templates as tmp
import prompt
from random import randint, choice


def right_answer(num1: str, num2: str, operator: str) -> str:
    return str(eval(num1 + operator + num2))


def main():
    name = tmp.greetings()
    print("What is the result of the expression?")

    for _ in range(3):
        operand1 = str(randint(1, 30))
        operand2 = str(randint(1, 30))
        operator = choice(['+', '-', '*'])

        print('Question: {} {} {}'.format(operand1, operator, operand2))
        user_answer = prompt.string('Your answer: ')

        if tmp.is_response_correct(
            user_answer,
            right_answer(operand1, operand2, operator),
            name
        ):
            continue
        else:
            break
    else:
        tmp.win(name)


if __name__ == "__main__":
    main()
