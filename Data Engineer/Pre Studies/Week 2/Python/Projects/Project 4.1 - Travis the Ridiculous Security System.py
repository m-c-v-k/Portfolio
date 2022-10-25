#! Python3

# Project 4 - Part 1 - Travis the Ridiculous Security System
# A program which handles users in a program.


known_users = ["Alice", "Bob", "Claire",
               "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
    print("Hi, my name is Travis.")
    name = input("What is your name?: ").strip().capitalize()
    print(name)

    if name in known_users:
        print("Name recognised.")
    else:
        print("Name not recognised.")
