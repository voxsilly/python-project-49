#!/usr/bin/env python3
from brain_games.logic import welcome_user, play_game
from brain_games.games.brain_even import game_logic
import sys
import os
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_game(name, game_logic)


if __name__ == '__main__':
    main()
