#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.game_logic import game
from brain_games.games.progression_game import progression_question


def rules():
    print('What number is missing in the progression?')


def main():
    greet()
    name = welcome_user()
    rules()
    game(progression_question, name)


if __name__ == '__main__':
    main()
