#! Python3

import random

# 1a
year_of_birth = input("Please enter year of birth?")

if year_of_birth.isnumeric() == True:
    print(year_of_birth)
else:
    print("Please enter a numeric value.")

# 1b

year_of_birth = input("Please enter year of birth?")

if year_of_birth.isnumeric() == True:
    year_of_birth = int(year_of_birth)
    if year_of_birth > 1900 and year_of_birth < 2020:
        print(year_of_birth)
    else:
        print("That is very unlikely.")
else:
    print("Please enter a numeric value.")

# 2
number = input("Write a positive number: ")
if (number.isnumeric()) or (number[1:].isnumeric() and number[0] == "-"):
    number = int(number)
    if number >= 0:
        print(f"The number: {number}")
    else:
        print("Number is not positive")
else:
    print(f"Could not convert {number} into a number, value set to -1")
    number = -1

# 3
year = int(input("Please enter a year: "))

if year % 4 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 4

prize = random.randint(1, 4)
doors = [1, 2, 3, 4]


guess = int(input("Guess between 1-4 where the prize is: "))

if guess == prize:
    print("You won!")
else:
    doors.remove(prize)
    doors.remove(guess)

    door = random.randint(0, 1)
    print(f"{doors[door]} has no price")
    guess_again = int(input("Guess again: "))
    if guess == prize:
        print("You won!")
    else:
        print("You lost!")
        print(f"The price was behind door number {door}!")
