#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def get_numbers():
    a = randint(1, 100)
    b = randint(1, 100)
    return a, b


def ask_question(a, b):
    answer = prompt.string(f"Question: {a} {b}\nYour answer: ")
    return answer


def interpret_answer(response, result):
    if response == result:
        print("Correct!")
        return True
    else:
        print(f"'{response}' is wrong answer ;(. Correct answer was {result}")
        return False


def find_gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def check_response(response):
    if isinstance(int(response), int):
        return True
    else:
        return False


def play(name):
    i = 0
    print("Find the greatest common divisor of given numbers.")
    while i < 3:
        i += 1
        a, b = get_numbers()
        answer = find_gcd(a, b)
        response = ask_question(a, b)
        verification = interpret_answer(int(response), answer)
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
