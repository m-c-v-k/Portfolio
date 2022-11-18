#! Python3

# Importing necessary libraries
import os


def finddir(dirname):
    path = 'C:\\Users\\mcvk\\Documents\\'

    for item in os.listdir(path):
        deep_path = path
        if os.path.isdir(path + item):
            if item == dirname:
                print(f"Item found in: {path}")
                return
            else:
                deep_path += item
                for item in os.listdir(deep_path):
                    if os.path.isdir(deep_path + item):
                        if item == dirname:
                            print(f"Item found in: {path}")
                            return

    print("Directory not found.")


find_me = input("Which Directory do you want to find: ")
finddir(find_me)
