### A simple program to print out a list as a string ###

my_list = ['test', 'cat', 'dog', 'frog', 'bamboo']


def comma_code(list):
    """ A small function to turn a list into a single string with a comma
        in between all list items.
    """

    list_as_string = ""

    for i in range(len(list)):
        if i in range(len(list) - 1):
            list_as_string += list[i] + ", "
        else:
            list_as_string += list[i]

    print(list_as_string)

    return list_as_string


comma_code(my_list)
