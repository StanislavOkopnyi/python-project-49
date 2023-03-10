import prompt

YES = "yes"
NO = "no"


def start_game(game, games_num: int = 3):

    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.QUESTION)

    for _ in range(games_num):
        right_answer, question = game.get_answer_and_question()
        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() != right_answer:
            print(f"'{user_answer}' is wrong answer ;(.", end="")
            print(f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f"Congratulations, {name}!")
