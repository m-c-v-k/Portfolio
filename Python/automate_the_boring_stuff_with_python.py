### Automate the Boring Stuff with Python ###
# This is a quick write of the programs meant to be writtenby the reader
# in the quite well-know book; Automate the Boring Stuff with Python.
# This is to showcase some of the basic knowledge I got in Python,
# as well as where it's from.

from decimal import DivisionByZero
import random
import sys

### Chapter 1 - Python Basics ###
### My First Program ###

'''
print('Hello World')
print('What\'s your name?')

my_name = input()

print('It\'s good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))

print('What\'s your age?')
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
'''


### Chapter 2 - Flow Control ###

'''
i = 0
while i <= 10:
    print(i)
    i += 1
'''


### Chapter 3 - Functions ###

'''
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
'''

'''
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
'''

### Chapter 4 - Lists ###
