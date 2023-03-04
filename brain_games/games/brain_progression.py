from random import randint


QUESTION = "What number is missing in the progression?"
PROGRESSION_START_SPREAD = (1, 50)
PROGRESSION_STEP_SPREAD = (1, 10)
PROGRESSION_LENGTH_SPREAD = (5, 10)


def get_answer_and_question() -> tuple:
    progression_start = randint(*PROGRESSION_START_SPREAD)
    progression_step = randint(*PROGRESSION_STEP_SPREAD)
    progression_length = randint(*PROGRESSION_LENGTH_SPREAD)
    element_to_guess = randint(0, progression_length - 1)

    element_of_progression = progression_start
    progression = []
    for _ in range(progression_length):
        progression.append(str(element_of_progression))
        element_of_progression += progression_step

    right_answer = int(progression[element_to_guess])
    progression[element_to_guess] = ".."
    return right_answer, ("Question: " + " ".join(progression))
