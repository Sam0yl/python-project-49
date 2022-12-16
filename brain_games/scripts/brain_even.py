#!/usr/bin/env python3

from brain_games.game_logic import game
from brain_games.games.even_game import even_question, rules


def main():
    game(even_question, rules)


if __name__ == '__main__':
    main()
