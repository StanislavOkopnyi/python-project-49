from brain_games.engine import FIRST_ANSWER, SECOND_ANSWER


def bool_to_str(answer: bool) -> str:
    if answer:
        return FIRST_ANSWER
    return SECOND_ANSWER
