#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.prime_game import prime_question, rules


def main():
    game(prime_question, rules)


if __name__ == '__main__':
    main()
