#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.game_logic import game
from brain_games.games.calc_game import calc_question, calc_check


def rules():
    print('What is the result of the exprassion?')


def main():
    greet()
    name = welcome_user()
    rules()
    game(calc_question, calc_check, name)


if __name__ == '__main__':
    main()
