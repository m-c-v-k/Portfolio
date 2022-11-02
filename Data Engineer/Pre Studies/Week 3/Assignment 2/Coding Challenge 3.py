#! Python3

'''
Coding Challenge 3 - Re-creating the 'Counter' functionality
Write a Python script that re-creates the Counter functionality in Python, see 
https://docs.python.org/3/library/collections.html#counter-objectsLinks to an external site. From 
the documentation: “It is a collection where elements are stored as dictionary keys and their 
counts are stored as dictionary values”. Actually, Counter is a class that supports more than we 
are going to do in this challenge, but don't worry about that for now 😊 

You must create a function called my_counter that takes in a single parameter. We are going to 
accept both strings and lists as input. You must loop over the input (so each character of a string
or each element of a list) and put the items into a dictionary as keys with the corresponding 
values being a counter of how many times each key is found in the input. Return this dictionary 
from the function. 

See a couple of examples below: 

my_counter("hello") returns a dict: {'h': 1, 'e': 1, 'l': 2, 'o': 1} 
my_counter("lallala") returns a dict: {'l': 4, 'a': 3} 
my_counter([1, 2, 1, 3]) returns a dict: {1: 2, 2: 1, 3: 1} 

Note: Like in week 2, you can use a defaultdict here to your advantage. If you feel up for it, try 
it out!
'''

# Importing necessary libraries
from collections import defaultdict

# Creating counter function


def my_counter(inp):

    # Creating a dictionary
    counter_dict = defaultdict(lambda: "Not present")

    # Check if item exist, add to existsing or add new entry
    for x in range(len(inp)):
        if inp[x] in counter_dict:
            counter_dict[inp[x]] += 1
        elif inp[x] not in counter_dict:
            counter_dict[inp[x]] = 1
    return counter_dict


# Run function with string and list
my_dict = my_counter('hello')
my_dict2 = my_counter('lallala')
my_dict3 = my_counter([1, 2, 1, 3])
print(my_dict)
print(my_dict2)
print(my_dict3)
