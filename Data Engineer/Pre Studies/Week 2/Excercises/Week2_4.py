#! Python3

'''
(Optional) Coding Challenge 4 - Dictionaries and key-value inputs v2
This challenge is optional. It is the same as challenge 3 with a dictionary, but you should research
how you can use a defaultdict instead of the ordinary dictionary in Python. Use the Python
documentation and a search engine to your advantage. This page might be useful, too
https://www.geeksforgeeks.org/defaultdict-in-python/ under 'Using List as default_factory'.
Note: When doing print(my_defaultdict) in Python the output looks like 'defaultdict(<class 'list'>,
{'Hello': ['hello', 'hrellololo'], '1': ['2']})', which is a bit different compared to the dictionary class in
challenge 3, but this is totally fine and expected 
'''

# Importing necessary libraries
from collections import defaultdict

# Welcome message
print("Welcome to the Default-Dictionaries and Key-Value Inputs program!")

# Create default dictionary
my_dict = defaultdict(lambda: "Not present")

# Control loop
while True:

    # Guide message
    print("Remember that you can always type 'print' to see the list or 'exit' to quit the " +
          "application")

    # Handler variables
    check_inp = True
    list_container = []

    # Handling user input loop
    while check_inp == True:

        # Getting user input
        user_inp = input(
            "Please enter two words seperated by a blank space: ").strip().capitalize()

        # Check if input is valid
        if len(user_inp.split(" ")) == 2:
            check_inp = False
            list_container += user_inp.split(" ")

        # Check if print command
        elif user_inp == "Print":
            print(my_dict)

        elif user_inp == "Exit":
            print(
                "It was nice to meet you, I'll print out the dictionary as a parting gift:")
            print(my_dict)
            print("Good bye!")
            quit()

    # Places input into dictionary
    if list_container[0] not in my_dict.keys():
        my_dict[list_container[0]] = [list_container[1]]
    elif list_container[0] in my_dict.keys() and list_container[1] not in my_dict[list_container[0]]:
        my_dict[list_container[0]].append(list_container[1])
