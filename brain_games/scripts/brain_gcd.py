#!/usr/bin/env python3
from brain_games.games import brain_gcd
from brain_games.games.templates.engine import engine


def main():
    engine(brain_gcd)


if __name__ == "__main__":
    main()
