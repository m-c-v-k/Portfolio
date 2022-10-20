#! Python3

# Project 1 - Crafting a Health Potion - Part 1
# A small program simulating the use of a health potions in a game.

# 4.16

import random

difficulty = 1
player_health = 50

health_potion = int(random.randint(25, 50) / difficulty)

player_health += health_potion

print(player_health)
