#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.progression_game import progression_question, rules


def main():
    game(progression_question, rules)


if __name__ == '__main__':
    main()
