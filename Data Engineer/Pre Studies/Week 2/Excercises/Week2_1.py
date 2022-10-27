#! Python3

'''
Coding Challenge 1 - Legal Drinking Age
Write a program to check if a person is of legal drinking age in Norway (18 years) or in the US (21
years). Create a script called week2_1.py for this challenge.
Ask the user their name, what year they are born in and where they live. Ensure that the user
inputs at
least two words as their name. The program should then return a short sentence describing the
verdict to the user.
Hint: You can use f.ex. len(your_string.split()) to get the length of the string your_string. Can 
you figure out why?
'''

# Importing necessary libraries
from datetime import date

# Getting required information from the user
user_inp = input(
    "Please enter your full name, year of birth, and country seperated by ' ' : ").strip().lower()

# Handling user_inp
user_info = user_inp.split(" ")

user_name = " ".join(user_info[:-2]).capitalize()
user_birth_year = int(user_info[-2])
user_country = user_info[-1]

# Calculate age
user_age = date.today().year - user_birth_year

# Check if the User is allowed to drink
if user_age >= 21 and user_country == "US":
    verdict = True
elif user_age >= 18 and user_country != "US":
    verdict = True
else:
    verdict = False

if verdict == True:
    print(f"Come on in {user_name}. As you're {user_age} years old and from {user_country} " +
          "you're allowed to drink!")
else:
    print(f"Please come back when you're old enough to drink {user_name}.")
