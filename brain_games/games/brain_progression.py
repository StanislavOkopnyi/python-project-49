#!/usr/bin/env python3
import brain_games.games.templates.conversation_templates as tmp
import prompt
from random import randint


def main():
    name = tmp.greetings()
    print("What number is missing in the progression")

    for _ in range(3):
        progression_start = randint(1, 50)
        progression_step = randint(1, 10)
        progression_length = randint(5, 10)
        element_to_guess = randint(0, progression_length - 1)

        element_of_progression = progression_start
        progression = []
        for _ in range(progression_length):
            progression.append(str(element_of_progression))
            element_of_progression += progression_step

        right_answer = progression[element_to_guess]
        progression[element_to_guess] = ".."
        print("Question: " + " ".join(progression))
        user_answer = prompt.string("Your answer: ")

        if tmp.is_response_correct(user_answer, right_answer, name):
            continue
        else:
            break
    else:
        tmp.win(name)


if __name__ == "__main__":
    main()
