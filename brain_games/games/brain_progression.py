from random import randint


QUESTION = "What number is missing in the progression"


def game() -> str | None:
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
    return right_answer
