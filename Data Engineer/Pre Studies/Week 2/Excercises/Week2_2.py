#! Python3¨

'''
Coding Challenge 2 - List of Names
Create a script called week2_2.py and make a program that reads in names from the command line
and saves these to a list. Use a special word like “PRINT” as input to print the current list. You  
can always end a running Python program with ctrl+c. Tell the user to use that to end the program!
When the program ends you should print a polite message and the list with all the names.
Remember that you can display a list simply with print(my_list) in Python.
Hint: You will need an infinite loop like from the Udemy course with 'while True: ...'.
'''

# Welcome message
print("Welcome to the List of Names!")

# Container for user input
name_list = []

# Control loop
while True:

    # Guide message
    print("Remember that you can always type 'print' to see the list or 'exit' to quit the " +
          "application")

    # Getting names from console
    user_inp = input("Please enter names seperated by a blank space ' ': "
                     ).strip().lower().split(" ")
    print("Thank you for your input!")

    # Handler name list
    name_list += user_inp

    for name in name_list:
        name_list[name_list.index(name)] = name.capitalize()

    # Check for keywords
    if "Print" in name_list:
        name_list.remove("Print")
        print('\n'.join(name_list))

    elif "Exit" in name_list:
        print("Thank you for using the List of Names! \nGood bye!")
        quit()
