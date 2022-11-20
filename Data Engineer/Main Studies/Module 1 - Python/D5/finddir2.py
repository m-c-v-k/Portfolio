#! Python3

# Importing necessary libraries
from pox.shutils import find

path = find('Portfolio', root='C:\\', type='dir')
print(path)
