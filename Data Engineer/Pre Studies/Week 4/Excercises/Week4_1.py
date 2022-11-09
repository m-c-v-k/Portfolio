#! Python3

"""
Coding Challenge 1 - Extending Counter from week 3
In this challenge we are going to turn our my_counter function from week 3 into a class and add
some functionality to it. You are of course welcome to reuse your code from week 3 where
applicable. We are going to need the following steps and functionality:
• Create a class called MyCounter (as it is costumery to capitalize class names in Python).
• Make a constructor that takes in one argument for the inps to count (apart from “self” of
course).
• Create the counter and save it to a field.
• Create a method called get that takes in a key and returns the count for that key. Make it
such that the method prints a message if the key is not found in the counter dictionary. It is
important that you do not throw an error here!
• Define the __str__ method to pretty print the counter dictionary.
"""

# Importing necessary libraries
from collections import defaultdict


class MyCounter:
    """ MyCounter class.
    """

    def __init__(self, inp):
        """ Constructor function, adds input to counter_dict.

        Args:
            inp (string/list): A string or list to be counted.
        """
        # Creating a default dictionary
        self.counter_dict = defaultdict(lambda: "Not present")

        # Check if items exists, add to existing or add new entry
        for x in range(len(inp)):
            if inp[x] in self.counter_dict:
                self.counter_dict[inp[x]] += 1
            elif inp[x] not in self.counter_dict:
                self.counter_dict[inp[x]] = 1

    def get(self, key_item):
        """ Prints the value for given key, gives not present if key does not exist.

        Args:
            key_item (string/int): A string or int to be checked against keys in counter_dict.
        """
        print(self.counter_dict[key_item])

    def __str__(self):
        """ Handles printing.

        Returns:
            string: A string printed with all keys and their corresponding values.
        """
        self.output = "The counter_dict contains:\n"

        for key, value in self.counter_dict.items():
            self.output += f"{key}: {value}\n"

        return self.output


# Functionality testing
print(MyCounter('lallala'))
MyCounter('lallala').get('o')
print(MyCounter('hello'))
x = MyCounter([1, 2, 3, 4, 2, 1, 3, 5, 7, 5, 3, 5, 6, 2, 3, 3])
x.get(2)
