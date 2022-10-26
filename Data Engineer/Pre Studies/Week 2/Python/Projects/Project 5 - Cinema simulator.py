#! Python3

# Project 5 - Cinema simulator!
# A Simple cinema emulator

# Dictionary of movies
films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

# Control-loop
while True:
    choice = input("Please enter which film you want to see: ").strip().title()

    # Check if choice is in the list
    if choice in films:

        # Check if the customer is old enough
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][0]:

            # Check if enough seats
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")

        else:
            print("You are too young to see that film.")

    else:
        print("We don't have that film yet.")
