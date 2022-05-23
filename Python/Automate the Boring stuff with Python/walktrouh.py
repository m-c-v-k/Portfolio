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
            print(answer)
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

'''
catNames = []
while True:
    print(' Enter a cat name ' + str(len(catNames) + 1) +
          ', or enter nothing to stop.')
    name = input()

    if name == '':
        break

    catNames = catNames + [name]

print('The cat names are:')
for name in catNames:
    print(name)
'''

'''
supplies = ['pens', 'staplers', 'phone', 'beer']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
'''

'''
messages = ['It is certain.',
            'It is decidedly so.',
            'Yes, definetely.',
            'Reply hazy, try agian.',
            'Ask again later.',
            'Concentrate and ask again.',
            'My reply is no.',
            'Outlook not so good.',
            'Very doubtful.']

print(messages[random.randint(0, len(messages) - 1)])
'''

'''
my_list = ['test', 'cat', 'dog', 'frog', 'bamboo']


def comma_code(list):
    """ A small function to turn a list into a single string with a comma
        in between all list items.
    """

    list_as_string = ""

    for i in range(len(list)):
        if i in range(len(list) - 1):
            list_as_string += list[i] + ", "
        else:
            list_as_string += list[i]

    print(list_as_string)

    return list_as_string


comma_code(my_list)
'''

'''
def character_picture_grid():
    """ Prints a list containing lists rotaded 90 degrees clock-wise.
    """
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if j < len(grid) - 1:
                print(grid[j][i], end="")
            else:
                print(grid[j][i])


character_picture_grid()
'''
