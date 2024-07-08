from random import randint


def game_logic():
    number = randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
