#!/usr/bin/env python3
from brain_games.logic import welcome_user, play_game
from brain_games.games.brain_progression import game_logic


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What number is missing in the progression?")
    play_game(name, game_logic)


if __name__ == '__main__':
    main()
