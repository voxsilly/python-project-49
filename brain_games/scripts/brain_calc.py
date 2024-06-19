#!/usr/bin/env python3
import prompt
from random import randint
from random import choice

def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello,", name)
    return name


def get_digits():
    a = randint(1, 100)
    b = randint(1, 100)
    return a, b


def get_operation(a, b):
    operations = choice('+-*')
    if operations == '+':
        operation = f"{a} {operations} {b}"
        return a + b, operation
    elif operations == '-':
        operation = f"{a} {operations} {b}"
        return a - b, operation
    else:
        operation = f"{a} {operations} {b}"
        return a * b, operation


def interpret_answer(response, result):
    if response == result:
        print("Correct!")
        return True
    else:
        print(f"'{response}' is wrong answer ;(. Correct answer was {result}")
        return False


def ask_question(operation):
    answer = prompt.string(f"Question: {operation}\nYour answer: ")
    return answer


def play(name):
    i = 0
    print("What is the result of the expression?")
    while i < 3:
        i += 1
        a, b = get_digits()
        operation = get_operation(a, b)
# print(operation[0])  подсказка с ответом, лучше ее удалить
        answer = ask_question(operation[1])
        verification = interpret_answer(int(answer), operation[0])
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
