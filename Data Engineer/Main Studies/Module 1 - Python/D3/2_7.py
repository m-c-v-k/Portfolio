#! Python3

# Importing necessary libraries
import numpy.random as npr

# 1a
rand_num = 1 + npr.randint(20)
guess_num = -1
game_over = False

while not (game_over):
    guess_num = int(input("Guess the number: "))

    if guess_num > rand_num:
        print("That was too high!")
    elif guess_num < rand_num:
        print("That was too low!")
    else:
        game_over = True

print(f"Correct! The number was: {rand_num}!")

# 1b
rand_num = 1 + npr.randint(20)
guess_num = -1
game_over = False
attempts = 0

while not (game_over):
    attempts += 1
    guess_num = int(input("Guess the number: "))

    if guess_num > rand_num:
        print("That was too high!")
    elif guess_num < rand_num:
        print("That was too low!")
    else:
        game_over = True
        print(
            f"Correct! The number was: {rand_num}, you guessed {attempts} times!")


# 1c
rand_num = 1 + npr.randint(20)
guess_num = -1
game_over = False
attempts = 0

while not (game_over):
    attempts += 1
    guess_num = int(input("Guess the number: "))

    if guess_num > rand_num:
        print("That was too high!")
    elif guess_num < rand_num:
        print("That was too low!")
    else:
        game_over = True
        print(
            f"Correct! The number was: {rand_num}, you guessed {attempts} times!")

    if attempts == 5:
        print("Game over!")
        game_over = True

# 2
car_fuel = 60
avg_fuel_consumption = 0.7
distance = 0

while (car_fuel > 0):
    distance += 10
    fuel_consumption_derivation = 0.5 - npr.rand()
    car_fuel -= (avg_fuel_consumption + fuel_consumption_derivation)

    check_fuel = car_fuel
    if (check_fuel - (avg_fuel_consumption + fuel_consumption_derivation)) < 0:
        print("I need more gas")
        break

print(f"drove {distance} km.")
print(f"Fuel remaining: {car_fuel} litres.")

# 3a
for num in range(1, 11):
    print(num)

# 3b
for num in range(15, 68, 7):
    print(num)

# 3c
val_1 = int(input("Select start value: "))
val_2 = int(input("Select end value: "))
for num in range(val_1, val_2 + 1):
    print(num)
