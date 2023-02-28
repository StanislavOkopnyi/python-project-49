import prompt


def start_game(game, games_num: int = 3):

    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))

    print(game.QUESTION)

    for _ in range(games_num):
        right_answer, question = game.get_answer_and_question()
        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer != right_answer:
            print(f"'{user_answer}' is wrong answer ;(.", end="")
            print(f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return None

        print('Correct!')

    print("Congratulations, {}!".format(name))
