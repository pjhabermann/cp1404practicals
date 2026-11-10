"""
CP1404 Practical
quick picks
"""
import random

NUMBERS = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45
)


def main():
    number_of_lines = int(input("How many quick picks? "))
    random_row = generate_random_row()
    print(random_row)


def generate_random_row():
    random_row = [random.choice(NUMBERS) for _ in range(6)]
    return random_row


main()
