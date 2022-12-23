#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.progression_game import progression_question, show_rules


def main():
    game(progression_question, show_rules)


if __name__ == '__main__':
    main()
