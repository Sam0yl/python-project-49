#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.calc_game import calc_question, show_rules


def main():
    game(calc_question, show_rules)


if __name__ == '__main__':
    main()
