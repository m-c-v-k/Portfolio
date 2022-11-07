#! Python3

# Project 9 - Part 1 - Make your own Coin!
# Creating a small coin class

class Pound:
    """A Base class for the coin 1 Pound
    """

    value = 1.00
    colour = "gold"
    num_edges = 1
    diameter = 22.5  # mm
    thickness = 3.15  # mm
    heads = True


# Some functionality testing
coin1 = Pound()

print(type(coin1))
print(coin1.value)
coin1.colour = "greenish"

coin2 = Pound()
print(coin1.colour)
print(coin2.colour)

coin1.value = 1.25
print(coin1.value)
print(coin2.value)
