#! python3

### Print Picnic Table ###

def print_picnic(item_dictionary, left_width, right_width):
    """ Prints a dictionary of picnic items so that it's easy to read.

    Args:
        item_dictionary (Dictionary): A dictionary containing items and ammount.
        left_width (Int): An integer decidning on how far the print will be
            adjusted
        right_width (Int): An integer decidning on how far the print will be
            adjusted
    """

    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in item_dictionary.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))


picnic_items = {
    'sandwiches': 4,
    'apples': 12,
    'cups': 4,
    'cookies': 8000
}

print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
