#! Python3

"""
Coding Challenge 2 - A Bit of Math
This challenge is about using Python for calculating math. You should create a python script 
week1_2.py for all the exercises. Use a comment to separate the three different sub exercises 
(remember you can comment a line in Python with a #).

You should display (print) the result of calculating the following expressions in Python:

The remainder of 345 after division with 12 (so the remainder after doing 345/12)
Create a variable x and set it to 5 and another variable y to 3. Overwrite x to have the value of 
x * y. Subtract 5 from x. Now display the result.
Your friend has 37 oranges and takes 6 for himself. He then splits the remaining oranges evenly 
between 3 of his friends (himself not included and evenly in the sense that everyone gets the same 
amount and an orange cannot be split into parts). How many oranges are left after all 3 friends 
have gotten their share? Write a python script to calculate this and print the result.
"""

# Sub-excercise 1
print(345 / 12)

# Sub-excercise 2
x = 5
y = 3
x *= y
x -= 5
print(x)

# Sub-excercise 3
oranges = 37
oranges -= 6
oranges %= 3
print(oranges)
