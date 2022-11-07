#! Python3

# Project 10 - Part 1 - Make all the Coins!
# Creating the coin class.

# Importing the necessary libraries

class Coin:
    def __init__(self, is_rare=False, clean=True, heads=True, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = is_rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def __del__(self):
        print("Coin spent")

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


class Pound(Coin):
    def __init__(self):
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
