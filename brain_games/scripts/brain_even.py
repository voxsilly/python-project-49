#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def get_random_number():  # get random number up to 100
    return randint(1, 100)


def is_correct_answer(number, answer):  # check if the answer is correct
    return (
        (number % 2 == 0 and answer == 'yes')
        or (number % 2 != 0 and answer == 'no')
    )


def correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def check_answer(number):  # get right answer. a bit excessive, but it works
    if number % 2 != 0:
        answer = "no"
        return answer
    elif number % 2 == 0:
        answer = "yes"
        return answer


def play(name):
    i = 0
    while i < 3:
        number = get_random_number()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if is_correct_answer(number, answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer(number)}'")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play(name)


if __name__ == '__main__':
    main()
