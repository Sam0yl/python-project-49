#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.game_logic import game
from brain_games.games.even_game import even_question


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    greet()
    name = welcome_user()
    rules()
    game(even_question, name)


if __name__ == '__main__':
    main()
