#! Python3

'''
Coding Challenge 3 - Dictionaries and key-value inputs
Create a script called week2_3.py for this challenge. In this challenge you should create a 
dictionary and take inputs to this from the command line. You must ensure the input is a valid 
key-value combination. One way of doing this is to take the length of the input 
(i.e. len(current_input.split(''))) and make sure that this is equal to two. Print an error message
if it is not and continue to accept input.

The dictionary must put values for the same key into a list. So, if a key does not exist in the
dictionary, create this together with a list consisting of one element (which is the value that was
input together with the key). If a key is already present in the dictionary, you should append the
value to the list, that is associated with the given key. Below is an example of input and how the
output must look like.

INPUT: Hello you
INPUT: Hi you
INPUT: Hello me
INPUT: END
OUTPUTS: {'Hello': ['you', 'me'], 'Hi': ['you']}

Like challenge 2 you should have a word for printing the dictionary and asking the user to use 
ctrl+c to end the script. And remember to have meaningful (and polite!) messages along the way for 
the user 
'''

# Welcome message
print("Welcome to the Dictionaries and Key-Value Inputs program!")

# Create dictionary
my_dict = {}

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
