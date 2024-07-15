#!/usr/bin/env python3
from brain_games.logic import welcome_user, play_game
from brain_games.games.brain_even import game_logic


def main():
    name = welcome_user()
    question_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(name, game_logic, question_text)


if __name__ == '__main__':
    main()
