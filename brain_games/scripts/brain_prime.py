#!/usr/bin/env python3
from brain_games.logic import welcome_user, play_game
from brain_games.games.brain_prime import game_logic


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    play_game(name, game_logic)


if __name__ == '__main__':
    main()
