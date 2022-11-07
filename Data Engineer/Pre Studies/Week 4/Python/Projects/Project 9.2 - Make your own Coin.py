#! Python3

# Project 9 - Part 2 - Make your own Coin!
# Creating a small coin class

# Importing the necessary libraries
import random


class Pound:

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5  # mm
        self.thickness = 3.15  # mm
        self.heads = True

    def rust(self):

        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):

        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin spent")


# Some functionality testing
coin1 = Pound(rare=True)
coin2 = Pound()

coin1.rust()


print(coin1.colour)
print(coin2.colour)
print(coin1.value)
print(coin2.value)

coin1.clean()
print(coin1.colour)

print(coin1.heads)
coin1.flip()
print(coin1.heads)
del coin2
