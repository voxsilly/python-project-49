from random import randint


def game_logic():
    start = randint(1, 10)
    step = randint(1, 5)
    length = 10
    progression = [start + step * i for i in range(length)]
    missing_index = randint(0, length - 1)
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
