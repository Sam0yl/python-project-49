#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.prime_game import prime_question, RULES


def main():
    game(prime_question, RULES)


if __name__ == '__main__':
    main()
