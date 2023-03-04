from typing import Any
import prompt

FIRST_ANSWER = "yes"
SECOND_ANSWER = "no"


def bool_to_str(answer: bool) -> str:
    if answer:
        return FIRST_ANSWER
    return SECOND_ANSWER


def convert_answer_to_str(answer: Any) -> str | None:
    if type(answer) is bool:
        return bool_to_str(answer)
    elif type(answer) is int:
        return str(answer)
    elif type(answer) is str:
        return answer


def start_game(game, games_num: int = 3):

    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.QUESTION)

    for _ in range(games_num):
        right_answer, question = game.get_answer_and_question()
        right_answer = convert_answer_to_str(right_answer)
        print(question)
        user_answer = prompt.string('Your answer: ').lower()

        if user_answer != right_answer:
            print(f"'{user_answer}' is wrong answer ;(.", end="")
            print(f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return None

        print('Correct!')

    print("Congratulations, {}!".format(name))
