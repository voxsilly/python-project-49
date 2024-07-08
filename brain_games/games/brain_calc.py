from random import randint, choice


def game_logic():
    a = randint(1, 100)
    b = randint(1, 100)
    operation = choice('+-*')
    if operation == '+':
        return f"{a} + {b}", str(a + b)
    elif operation == '-':
        return f"{a} - {b}", str(a - b)
    else:
        return f"{a} * {b}", str(a * b)
