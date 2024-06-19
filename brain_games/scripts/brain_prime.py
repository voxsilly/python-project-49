#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def get_number():
    a = randint(1, 100)
    return a


def ask_question(a):
    answer = prompt.string(f"Question: {a}\nYour answer: ")
    return answer


def interpret_answer(response, result):
    if response == result:
        print("Correct!")
        return True
    else:
        print(f"'{response}' is wrong answer ;(. Correct answer was '{result}'")
        return False


def check_prime(number):
    flag = False
    word = ''
    if number == 1:
        word = 'no'
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
    if flag:
        word = 'no'
    else:
        word = 'yes'
    return word


def play(name):
    i = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:
        i += 1
        number = get_number()
        answer = check_prime(number)
        response = ask_question(number)
        verification = interpret_answer(response, answer)
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
