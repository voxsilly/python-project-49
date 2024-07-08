from random import randint
from math import gcd


def game_logic():
    a = randint(1, 100)
    b = randint(1, 100)
    return f"{a} {b}", str(gcd(a, b))
