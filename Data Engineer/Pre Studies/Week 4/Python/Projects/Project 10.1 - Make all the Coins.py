#! Python3

# Project 10 - Part 1 - Make all the Coins!
# Creating the coin class.

# Importing the necessary libraries.
import random


class Coin:
    """ Parent class for different types of coins.
    """

    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        """ Constructor function

        Args:
            is_rare (bool, optional): Lets the user define is coin is rare or not. Defaults to False.
            clean (bool, optional): Lets the user define if the coin is clean or not. Defaults to True.
            heads (bool, optional): Lets the user define is the coin is heads or tails. Defaults to True.
        """

        # Adds coin-specific data to the coin.
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Non coin-specific data.
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        # Rarity / Value.
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        # Clean / Colour.
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def __del__(self):
        """ Handles coin destruction.
        """

        print("Coin spent.")

    def rust(self):
        """ Handles colour depending on rusty or not.
        """

        self.colour = self.rusty_colour

    def clean(self):
        """ Handles colour if a coin is cleaned.
        """

        self.colour = self.clean_colour

    def flip(self):
        """ Simulates flipping a coin (heads or tails).
        """

        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


class Pound(Coin):
    def __init__(self):
        """ Constructor function, importing everything from Coin.
            Unpacks data into Coin.
        """

        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)


# Some functionality testing
one_pound_coin = Pound()
print(one_pound_coin.colour)
one_pound_coin.rust()
print(one_pound_coin.colour)
