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
print("Welcome to the")
