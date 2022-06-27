#! python3
# z_fix.py
# A simple program to calculate the new z-position for laser measurement,
# using a measured value on a fixed height.

import ast
import os
import re


def z_fix():
    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt')), 'r') as f:
        data = f.read()
        eval_data = ast.literal_eval(data)

    while True:

        # Print all fix locations and their z-coordinate.
        for num in range(len(eval_data)):
            places = list(eval_data.keys())
            fix_position = eval_data[places[num]]

            print(str(places[num]) + ': ' + str(fix_position))

        # Select existing fix location or new
        selected = str(
            input('Please enter your desired Z-location, ' +
                  'create a new, change z, edit, delete, or quit.\n'))

        if selected.lower() == 'new':
            new_fix(eval_data)
        elif selected.lower() == 'edit':
            edit_fix(eval_data)
        elif selected.lower() == 'change z':
            change_z()
        elif selected.lower() == 'delete':
            delete_fix(eval_data)
        elif selected.lower() == 'quit':
            delete_file('measured.txt')
            print("Good bye.")
            break
        else:
            for i in places:
                if selected.lower() == str(i).lower():
                    set_z(eval_data[i])
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

    placement = input('Please enter the placement of the fixed position:\n')
    height = test_z()

    adder = eval_data
    adder[placement] = height
    print(adder)

    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt')), 'w') as f:
        add_data = f.write(str(adder))

    return mo


def change_z():
    '''change_z Changes the current Z-position and tells the user what
    measure to put the laser to.

    Returns:
        Float: A float containing the new measured value.
    '''

    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'measured.txt'))) as f:
        data = f.read()

        eval_data = ast.literal_eval(data)

    z = list(eval_data.keys())
    m = list(eval_data.values())
    z_position = z[0]
    old_measured = m[0]

    test_z()

    z_position = float(z_position)
    change_by = z_position - desired_z
    new_measured = old_measured + change_by * 100

    print("Set the laser to: " + str(new_measured) + '.')
    save_current(desired_z, new_measured)

    return new_measured


def set_z(z_position):
    '''set_z let's the user save the measured z-fix measurement.

    Args:
        z_position (string): A string containing the measured z_fix position.
    '''

    measured_z = float(
        input("What is the current measurement for the fix position?\n"))

    ###

    print(str(z_position) + " set to " + str(measured_z) + ".")
    save_current(z_position, measured_z)


def save_current(z_pos, measured):
    '''save_current saves the current z-position and measurement, in order
    to allow the user to change from the current position to a new one.

    Args:
        measured (Float): A float containing the position on the measure-stick.
        z_pos (Float): The z-position that is being measured.

    Returns:
        Dictionary: A dictionary over the latest measurement.
    '''

    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'measured.txt')), 'w+') as f:
        new_save = {}
        new_save[z_pos] = measured
        save_data = f.write(str(new_save))

    return new_save


def delete_file(file):
    '''delete_file Deletes a specified file

    Args:
        file (String): The file name of the file to be deleted.
    '''

    if os.path.exists(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', file))):
        os.remove(str(os.getcwd()) + str(os.path.join('\\',
                  'Python', 'My_Projects', 'z_fix', file)))
    else:
        print("The file does not exist.")


def delete_fix(eval_data):
    '''delete_fix let's the user delete a saved fixed position.

    Args:
        eval_data (Dictionary): The dictionary containing all fixed positions.

    Returns:
        Dictionary: The dictionary containing all fixed positions.
    '''

    usr_inp = input("Please enter the fix you'd like to remove:\n")

    # TODO

    eval_data.pop(usr_inp)

    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt')), 'w+') as f:

        f.write(str(eval_data))

    return eval_data


def edit_fix(eval_data):
    '''edit_fix Let's the user edit a chosen fixed position.

    Args:
        eval_data (Dictionary): The dictionary containing all fixed positions.

    Returns:
        Dictionary: The dictionary containing all fixed positions.
    '''

    usr_inp_fix = input("Please enter the fix you'd like to edit:\n")
    usr_inp_pos = test_z()

    eval_data[usr_inp_fix] = usr_inp_pos

    with open(str(os.getcwd()) + str(os.path.join('\\', 'Python', 'My_Projects', 'z_fix', 'fix.txt')), 'w+') as f:

        f.write(str(eval_data))

    return eval_data


def test_z():

    while True:
        try:
            # Controll the z-cordinates
            desired_z = input("Please enter the desired Z-position:\n")
            cordinate_test = re.compile(r"\d+\.\d{3}")
            mo = re.fullmatch(cordinate_test, desired_z)
            if mo is None:
                x
            break

        except:
            print("Please enter digits and seperator '.' only.")

    return desired_z


def test_measure():
    while True:
        try:
            # Controll the measure
            desired_measure = float(
                input("Please enter the measured height:\n"))
            measure_test = re.compile(r"\d[1,3]\.\d{1}")
            mo = re.fullmatch(measure_test, desired_measure)
            if mo is None:
                x
            break

        except:
            print("Please enter digits and seperator'.' only.")

    return desired_measure


z_fix()
