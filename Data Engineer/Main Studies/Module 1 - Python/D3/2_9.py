#! Python3

# Importing necessary libraries
import random
from collections import defaultdict


# 1a
def get_user_initials():
    usr_inp = input("Please enter your name: ")


get_user_initials()

# 1b


def get_user_initials():
    usr_inp = input("Please enter your name: ")
    usr_name = split_name(usr_inp)


def split_name(name):
    name = name.split()
    first_name = name[0]
    last_name = name[1]

    return first_name, last_name


get_user_initials()

# 1c


def get_user_initials():
    usr_inp = input("Please enter your name: ").title()
    first_name, last_name = split_name(usr_inp)
    initials = f"{first_name[0]}.{last_name[0]}."
    print(initials)


def split_name(name):
    name = name.split()
    first_name = name[0]
    last_name = name[1]

    return first_name, last_name


get_user_initials()

# 2a


def roll_dice(sides):
    dice = random.randint(1, sides)
    print(dice)


roll_dice(3)

# 2b


def roll_dice(sides, num_dice):
    dice = 0

    for i in range(num_dice):
        dice += random.randint(1, sides)
        print(i)

    print(dice)


roll_dice(6, 5)


# 2c

def roll_dice(sides, num_dice):
    dice = []

    for i in range(num_dice):
        dice.append(random.randint(1, sides))

    print(dice)


roll_dice(6, 3)


# 3a
num_list = []


def serial_number(times):

    for x in range(times):
        serial = ""
        while serial not in num_list:
            serial = random.randint(10000000, 99999999)

            if serial not in num_list:
                num_list.append(serial)


serial_number(10)
print(num_list)

# 3b
serials = defaultdict(lambda: "Item not found")


def serial_number(key):
    serial = ""

    if key not in (serials.keys()):

        while serial not in serials.values():
            serial = random.randint(10000000, 99999999)

            if serial not in serials:
                serials[key] = serial
                break


serial_number("mooo")
print(serials)

# 4a


def reverser(inp_list):

    inp_list = inp_list[::-1]
    print(inp_list)


reverser([1, 2, 3])


def reverser(inp_list):
    """ Sorts a list in descending

    Args:
        inp_list (list): List containing the values to be sorted.
    """

    # List length
    n = len(inp_list)

    # Optimizing the code, if no change is needed it won't have to do everything.
    swapped = False

    # Go through all entries in the list, there is no need for the last element.
    for i in range(n-1):

        # Go through the list up to the second last to current value (i)
        for j in range(n-i-1):

            # If j is bigger than the next item, swap place
            if inp_list[j] < inp_list[j + 1]:
                swapped = True
                inp_list[j], inp_list[j + 1] = inp_list[j + 1], inp_list[j]

        # If there is no need for any swaps by now, there won't be any swaps
        # Exit loop
        if not swapped:
            # Break function
            return


my_list = [64, 34, 25, 12, 22, 11, 90]
reverser(my_list)
print(my_list)
