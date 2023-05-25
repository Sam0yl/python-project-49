#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.progression_game import progression_question, RULES


def main():
    game(progression_question, RULES)


if __name__ == '__main__':
    main()
