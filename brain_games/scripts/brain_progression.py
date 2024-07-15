#!/usr/bin/env python3
from brain_games.logic import welcome_user, play_game
from brain_games.games.brain_progression import game_logic


def main():
    name = welcome_user()
    question_text = "What number is missing in the progression?"
    play_game(name, game_logic, question_text)


if __name__ == '__main__':
    main()
