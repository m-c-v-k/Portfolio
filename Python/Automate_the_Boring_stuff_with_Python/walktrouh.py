#! python3

### Automate the Boring Stuff with Python ###
# This is a quick write of the programs meant to be writtenby the reader
# in the quite well-know book; Automate the Boring Stuff with Python.
# This is to showcase some of the basic knowledge I got in Python,
# as well as where it's from.

from decimal import DivisionByZero
import random
import sys
import pprint
import pyperclip

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

### Chapter 5 - Dictionaries and Structuring Data ###

'''
birthdays = {'Alice': 'April 1', 'Bob': 'December 12', 'Carol': 'March 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have the birthday information for ' + name)
        print('What is their birthday?')
    bday = input()
    birthdays[name] = bday
    print('Birthday database updated.')
'''

'''
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')

print(spam)
'''

'''
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
'''

the_board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

'''
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'

for i in range(9):
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'


print_board(the_board)
'''

all_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'sandwiches': 3, 'apples': 1},
    'Carol': {'cups': 3, 'pies': 3}
}

'''
def total_brought(guests, item):
    """ Checks for the total amount of items brought.

    Args:
        guests (Dictionary): A dictionary over all guests and what
            they are brining in a subdictionary.
        item (String): The item you want to check for.

    Returns:
        Int: Returns the ammount fo the specified item that is brought,
            0 items by default.
    """

    num_brought = 0

    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)

    return num_brought


print('Number of things being brought:')
print(' - Apples ' + str(total_brought(all_guests, 'apples')))
print(' - Cups ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'sandwiches')))
print(' - Apple Pies ' + str(total_brought(all_guests, 'pies')))
'''

inventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

dragon_loot = [
    'gold coin',
    'dagger',
    'ruby',
    'gold coin',
    'gold coin',
    'dragon\'s tooth'
]

'''
def display_inventory(inventory):
    """ Displays the player ionventory with ammount item.

    Args:
        inventory (Dictionary): A dictionary over items and the ammount of the items.
    """

    print('Inventory:')
    item_total = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v

    print('Total number of items: ' + str(item_total))


def add_to_inventory(inventory, added_items):
    """ Adds items to the inventory

    Args:
        inventory (Dictionary): A dictionary over items and the ammount of the items.
        added_items (List): A list over items to add to the inventory.
    """

    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    print('Items added to your inventory.')


display_inventory(inventory)
add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
'''


### Chapter 6 - Manipulating Strings ###

'''
while True:
    print("Enter your age.")
    age = input()

    if age.isdecimal():
        break

    print("PLease enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only):")
    password = input()

    if password.isalnum():
        break

    print("Passwords can only have letters and numbers.")
'''

'''
def print_picnic(item_dictionary, left_width, right_width):
    """ Prints a dictionary of picnic items so that it's easy to read.

    Args:
        item_dictionary (Dictionary): A dictionary containing items and ammount.
        left_width (Int): An integer decidning on how far the print will be
            adjusted
        right_width (Int): An integer decidning on how far the print will be
            adjusted
    """

    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in item_dictionary.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))


picnic_items = {
    'sandwiches': 4,
    'apples': 12,
    'cups': 4,
    'cookies': 8000
}

print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
'''

'''
passwords = {
    'e-mail': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account name ' + account)
'''

'''
text = pyperclip.paste()

# Seperate lines and add stars

lines = text.split('\n')

for i in range(len(lines)):     # Loop throught ass indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # Add star to each string in 'lines' list

text = '\n'.join(lines)

pyperclip.copy(text)
'''

'''
table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

def print_table(table_data):
    """ Takes a list containing other lists and prints it neatly and right justified

    Args:
        table_data (List): A List containing other lists.
    """

    column_width = [0] * len(table_data)

    for i, column_data in enumerate(table_data):

        for row_item in column_data:
            item_length = len(row_item)

            if item_length > column_width[i]:
                column_width[i] = item_length

    num_columns = len(table_data)
    num_rows = len(table_data[0])

    for row_index in range(num_rows):

        for column_index in range(num_columns):
            print(table_data[column_index][row_index].rjust(
                column_width[column_index]), end=' ')
        print('')


print_table(table_data)
'''

### Part II - Automating tasks ###


def is_phone_number(text):
    """ Checking if the text is a phone number or not.

    Args:
        text (string): String to be checked if it's a phone number or not.

    Returns:
        boolean: False if not a phone number (US standard), else True if it's a phone number
    """

    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


def find_phone_number(text):
    """ Takes a string and checks if it contains any phone numbers.

    Args:
        text (string): A string to be chacked for any potential phonenumbers. 
    """
    for i in range(len(text)):

        chunk = text[i:i+12]

        if is_phone_number(chunk):
            print('Phone number found: ' + chunk)

    print('Search finished.')


find_phone_number(
    'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
