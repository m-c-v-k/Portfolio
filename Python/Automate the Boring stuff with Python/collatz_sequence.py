#! python3

### A program running the Collatz Sequence ###

import sys

""" A program that runs the Collatz Sequence,
        which no matter what number above 0, it'll
        always end by returning 1.
    """


def collatz_sequence():
    inp = 1

    try:
        inp = int(input(' Please enter an integer:\n'))
        if inp <= 0:
            print(
                'Divisions by 0 and negative numbers are out of reach for mere mortals.')
            collatz_sequence()
    except ValueError as ex:
        collatz_sequence()

    while inp != 1:

        if inp % 2 == 0:
            inp = inp // 2
        elif inp % 2 == 1:
            inp = inp * 3 + 1

        print(inp)

    sys.exit()


collatz_sequence()
