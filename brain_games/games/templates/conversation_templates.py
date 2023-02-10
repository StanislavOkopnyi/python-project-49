import prompt


def greetings() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def lose(name: str) -> None:
    print("Let's try again, {}!".format(name))


def win(name: str) -> None:
    print("Congratulations, {}!".format(name))


def is_response_correct(user_answer: str, right_answer: str, name: str) -> bool:
    if user_answer == right_answer:
        print('Correct!')
        return True
    else:
        print("'{}' is wrong answer ;(.".format(user_answer), end="")
        print(" Correct answer was '{}'.".format(
              right_answer))
        lose(name)
        return False
