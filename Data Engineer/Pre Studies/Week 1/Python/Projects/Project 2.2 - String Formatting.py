#! Python3

# Project 2 - Collecting Data - Part 2
# A small program collecting Data

# Ask user for name
user_name = input("Please enter your name: ")

# Ask user for age
user_age = input("Please enter your age: ")

# Ask user for city
user_city = input("Please enter your city: ")

# ask user what they enjoy
user_enjoy = input("Please enter what you enjoy: ")

# Create output text
output = f"""Your name is {user_name} and you are {user_age} years old.
You live in {user_city} and you love {user_enjoy}."""

# Print output to screen
print(output)
