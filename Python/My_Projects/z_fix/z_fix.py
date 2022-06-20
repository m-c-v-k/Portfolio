#! python3
# z_fix.py
# A simple program to calculate the new z-position for laser measurement,
# using a measured value on a fixed height.

import ast
import os
import re


def z_fix():
    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt'))) as f:
        data = f.read()

    eval_data = ast.literal_eval(data)

    # Print all fix locations and their z-coordinate.
    for num in range(len(eval_data)):
        places = list(eval_data.keys())
        fix_position = eval_data[places[num]]

        print(str(places[num]) + ': ' + str(fix_position))

    while True:
        # Select existing fix location or new
        selected = str(
            input('Please enter your desired Z-location, create a new, edit, remove, or quit.\n'))

        if selected.lower() == 'new':
            new_fix(eval_data)
        elif selected.lower() == 'edit':
            print("oops")
        elif selected.lower() == 'remove':
            print("oops")
        elif selected.lower() == 'quit':
            print("Good bye.")
            break
        else:
            for i in places:
                if selected.lower() == str(i).lower():
                    calculate_z(eval_data[i])
                    break
                elif i == places[-1]:
                    print("That is not a valid choice, please try again.")
                else:
                    pass

    return None


def new_fix(eval_data):
    ''' new_fix lets the user create and save a new fixed position

    Args:
        eval_data (Dictionary): A Dictionary over all saved fixed positions.

    Returns:
        NoneType: Returns a matchobject or None.
    '''
    placement = input(
        'Please enter the placement of the fixed position:\n')

    while True:
        try:
            # Controll the z-cordinates
            height = input('Please enter the Z-index of the fixed position:\n')
            cordinate_test = re.compile(r"\d+\.\d{3}")
            mo = re.fullmatch(cordinate_test, height)
            if mo is None:
                x
            break

        except:
            print("Please enter digits and seperator '.' only.")

    adder = eval_data
    adder[placement] = height
    print(adder)

    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt')), 'w') as f:
        add_data = f.write(str(adder))

    return mo


def calculate_z(z_position):

    measured_z = float(
        input("What is the current measurement for the fix position?\n"))
    desired_z = float(input("Please enter the desired Z-position.\n"))

    z_position = float(z_position)
    change_by = z_position - desired_z
    set_position = measured_z - abs(change_by) * 100

    if z_position < desired_z:
        print("You need to raise the laser measurer with " +
              str(set_position) + ' centimeters.')
    elif desired_z > z_position:
        print("You need to lower the laser measurer with " +
              str(set_position) + ' centimeters.')
    else:
        print("There's no need to change the laser measurement.")


z_fix()
