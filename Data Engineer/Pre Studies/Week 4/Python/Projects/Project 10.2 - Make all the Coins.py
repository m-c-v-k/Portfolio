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

    def __str__(self):
        if self.original_value >= 1:
            return f"£{int(self.original_value)} Coin"
        else:
            return f"{int(self.original_value * 100)}p Coin"

    def rust(self):
        """ Handles colour depending on rusty or not.
        """

        self.colour = self.rusty_colour

    def clean(self):
        """ Handles colour is a coin is cleaned.
        """

        self.colour = self.clean_colour

    def flip(self):
        """ SImulates flipping a coin (heads or tails).
        """

        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


class One_Pound(Coin):
    """ Defines the One_Pound class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
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


class One_Pence(Coin):
    """ Defines the One_Pence class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
        """

        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }
        super().__init__(**data)


class Two_Pence(Coin):
    """ Defines the Two_Pence class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
        """

        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }
        super().__init__(**data)


class Five_Pence(Coin):
    """ Defines the Five_Pence class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
        """

        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }
        super().__init__(**data)

        def rust(self):
            """ Handles colour depending on rusty or not.
            """
            self.colour = self.clean_colour

        def clean(self):
            """ Handles colour if a coin is cleaned.
            """
            self.colour = self.clean_colour


class Ten_Pence(Coin):
    """ Defines the Ten_Pence class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
        """

        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
        }
        super().__init__(**data)

        def rust(self):
            """ Handles colour depending on rusty or not.
            """
            self.colour = self.clean_colour

        def clean(self):
            """ Handles colour if a coin is cleaned.
            """
            self.colour = self.clean_colour


class Twenty_Pence(Coin):
    """ Defines the Twenty_Pence class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
        """

        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
        }
        super().__init__(**data)

        def rust(self):
            """ Handles colour depending on rusty or not.
            """
            self.colour = self.clean_colour

        def clean(self):
            """ Handles colour if a coin is cleaned.
            """
            self.colour = self.clean_colour


class Fifty_Pence(Coin):
    """ Defines the Fifty_Pence class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
        """

        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8
        }
        super().__init__(**data)

        def rust(self):
            """ Handles colour depending on rusty or not.
            """
            self.colour = self.clean_colour

        def clean(self):
            """ Handles colour if a coin is cleaned.
            """
            self.colour = self.clean_colour


class Two_Pound(Coin):
    """ Defines the Two_Pound class.

    Args:
        Coin (class): Coin parent class.
    """

    def __init__(self):
        """ Constructor function importing everything from Coin.
            Upacks data into Coin.
        """

        data = {
            "original_value": 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.5,
            "mass": 12.00
        }
        super().__init__(**data)


# Some functionality testing
coins = [
    One_Pence(),
    Two_Pence(),
    Five_Pence(),
    Ten_Pence(),
    Twenty_Pence(),
    Fifty_Pence(),
    One_Pound(),
    Two_Pound()
]

for coin in coins:
    arguments = [
        coin,
        coin.colour,
        coin.value,
        coin.diameter,
        coin.thickness,
        coin.num_edges,
        coin.mass
    ]

    string = "{} - Colour: {}, value: {}, diameter(mm): {}, thickness(mm): {}, number of edges: {}, mass(g): {}".format(
        *arguments)

    print(string)
