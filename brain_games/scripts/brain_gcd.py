#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.game_logic import game
from brain_games.games.gcd_game import gcd_question


def rules():
    print('Find the greatest common divisor of given numbers.')


def main():
    greet()
    name = welcome_user()
    rules()
    game(gcd_question, name)


if __name__ == '__main__':
    main()
