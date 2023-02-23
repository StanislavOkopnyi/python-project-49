import prompt


def engine(game, games_num: int = 3):

    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))

    print(game.QUESTION)

    for _ in range(games_num):
        right_answer = game.game()
        user_answer = prompt.string('Your answer: ')

        if user_answer != right_answer:
            print("'{}' is wrong answer ;(.".format(user_answer), end="")
            print(" Correct answer was '{}'.".format(right_answer))
            print("Let's try again, {}!".format(name))
            break

        print('Correct!')

    else:
        print("Congratulations, {}!".format(name))
