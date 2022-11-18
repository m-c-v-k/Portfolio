#! Python3

# Importing necessary libraries
import sys
import os

# 1q
print(os.listdir())

# 1b
print(os.listdir('C:\\'))

# 1c
path = 'C:\\Users\\mcvk\\Documents\\'
for item in os.listdir('C:\\Users\\mcvk\\Documents\\'):
    if os.path.isdir(path + item):
        print(f"{item}:\tDirectory")
    elif os.path.isfile(path + item):
        print(f"{item}:\tFile\t{os.stat(path + item).st_size}")

# 1d
path = 'C:\\Users\\mcvk\\Documents\\'
for item in os.listdir('C:\\Users\\mcvk\\Documents\\'):
    if os.path.isdir(path + item):
        print(f"{item}:\tDirectory")
    elif os.path.isfile(path + item):
        print(f"{item}:\tFile")

# 2
for item in os.listdir('C:\\Users\\mcvk\\Documents\\'):
    if item == 'description.dsc':
        print("Exists")
    else:
        f = open(str(path + "description.dsc"), "w+")
        output = ""
        for item in os.listdir('C:\\Users\\mcvk\\Documents\\'):
            output += f"{item}\t-\n"
        f.write(output)
        f.close()

# 3 Different file.
