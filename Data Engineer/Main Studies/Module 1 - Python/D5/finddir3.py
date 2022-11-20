#! Python3

# Importing necessary libraries
import os

for root, dirs, files in os.walk('C:\\', topdown=True):
    if "Portfolio" in root:
        print(root)
        break
