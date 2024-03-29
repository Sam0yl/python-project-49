#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.gcd_game import gcd_question, RULES


def main():
    game(gcd_question, RULES)


if __name__ == '__main__':
    main()
