#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def getrand():  # get random number up to 100
    return randint(1, 100)


def check_right(answer, number):  # check if the answer is correct
    if number % 2 == 0 and answer == 'yes':
        return True
    elif number % 2 != 0 and answer == 'no':
        return True
    else:
        return False


def check_answer(number):  # get right answer. a bit excessive, but it works
    if number % 2 != 0:
        answer = "no"
        return answer
    elif number % 2 == 0:
        answer = "yes"
        return answer


def play(name):
    i = 0
    number = getrand()
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if check_right(answer, number) is False:
        print(f"'{answer}' is wrong answer ;(.\
Correct answer was '{check_answer(number)}'")
        print(f"Let's try again, {name}")
    elif check_right(answer, number):
        print('Correct!')
        while i < 2 and check_right(answer, number):
            i += 1
            number = getrand()
            print(f'Question: {number}')
            answer = prompt.string('Your answer: ')
            if check_right(answer, number):
                print("Correct!")
            else:
                print(f"'{answer}' is wrong answer ;(.\
 Correct answer was '{check_answer(number)}'")
                print(f"Let's try again, {name}")
    if i == 2 and check_right(answer, number):
        print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play(name)


if __name__ == '__main__':
    main()
