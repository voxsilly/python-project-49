#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def get_progression():  # a - длина прогрессии, b - начальная точка, c — шаг
    a = randint(5, 10)
    b = randint(1, 20)
    c = randint(1, 10)
    progression = []
    for i in range(a):
        element = b + i * c
        progression.append(element)
    return progression


def get_copy(progression):
    a = randint(0, len(progression) - 1)
    result = []
    for i in range(len(progression)):
        if i == a:
            element = ".."
            result.append(element)
        else:
            element = progression[i]
            result.append(element)
    return progression[a], result


def ask_question(progression):
    line = " ".join(map(str, progression))
    response = prompt.string(f"Question: {line}\nYour answer: ")
    return response


def interpret_answer(response, result):
    if response == result:
        print("Correct!")
        return True
    else:
        print(f"'{response}' is wrong answer ;(. Correct answer was {result}")
        return False


def play(name):
    i = 0
    print("What number is missing in the progression?")
    while i < 3:
        i += 1
        pro = get_progression()
        cop = get_copy(pro)
        response = ask_question(cop[1])
        verification = interpret_answer(int(response), cop[0])
        if verification is False:
            print(f"Let's try again, {name}!")
            break
    if verification is True:
        print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    play(name)


if __name__ == '__main__':
    main()
