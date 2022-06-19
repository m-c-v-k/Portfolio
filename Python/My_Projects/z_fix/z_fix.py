#! python3
# z_fix.py
# A simple program to calculate the new z-position for laser measurement,
# using a measured value on a fixed height.

import ast
import os
import re


def z_fix():

    return


def fix_handler():
    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt'))) as f:
        data = f.read()

    eval_data = ast.literal_eval(data)

    #js_data = json.loads(data)

    # Print all fix locations and their z-coordinate.
    for num in range(len(eval_data)):
        places = list(eval_data.keys())
        fix_position = eval_data[places[num]]

        print(str(places[num]) + ': ' + str(fix_position))

    # Select existing fix location or new
    selected = str(
        input('Please enter your desired Z-location, create a new, remove, or cancel.\n'))

    if selected.lower() == 'new':

        placement = input(
            'Please enter the placement of the fixed position:\n')

        try:
            # Controll the z-cordinates
            height = input('Please enter the Z-index of the fixed position:\n')
            cordinate_test = re.compile(r"\d{0,4}\.\d{3}")
            mo = cordinate_test.search(height)
            print(mo)
            mo != None
        except TypeError as e:
            print("Please enter digits and seperator '.' only.")
            raise e

        adder = eval_data
        adder[placement] = height
        print(adder)

        with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt')), 'w') as f:
            add_data = f.write(str(adder))

    elif selected.lower() == 'cancel':
        print("oops")
    elif selected.lower() == 'remove':
        print("oops")
    else:
        # TODO
        print("oops")

        # Remove fix location


fix_handler()
