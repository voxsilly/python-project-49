#!/usr/bin/env python3
from logic import welcome_user
import sys
import os
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def main():
    print("Welcome to the Brain Games!")
    welcome_user()


if __name__ == '__main__':
    main()
