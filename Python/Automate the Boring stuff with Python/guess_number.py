### A basic Guess Number program ###

import random
import sys


def guess_number(counter):
    """ A function for a basic guess the number game, where the user has 3 guesses.
    Checks the input if it's an integer or not, if it's not the user will be asked
    to enter a new input, without losing any turns.

    Args:
        counter (int): number of used turns

    Returns:
        int: Returns the controller, 0 = Failed to guess the number, 1 = correctly 
        guessed the number.
    """

    count = counter
    correct = random.randint(1, 10)
    controller = 0
    answer = ""
    inp = ""

    print('Guess a number between 1 and 10, you have ' +
          str(3 - count) + ' tries to guess the correct number')

    while count < 3 or controller == 1:

        try:
            inp = int(input('Enter a number between 1 and 10: '))
        except ValueError as ex:
            print('Please enter an integer.')
            guess_number(count)

        count += 1

        if inp == correct:
            answer = "Correct! Your guessed the number in " + \
                str(count) + " tries."
            controller = 1
            print(answer)
            sys.exit()

        elif inp < correct:
            answer = "The number you are looking for is larger than " + \
                str(inp)

        elif inp > correct:
            answer = "The number you are looking for is smaller than " + \
                str(inp)

        print(answer)

    if count == 3:
        answer = "You failed to guess the correct number: " + str(correct)
        print(answer)

    return controller


guess_number(0)
