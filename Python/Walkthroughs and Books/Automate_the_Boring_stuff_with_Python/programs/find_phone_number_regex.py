#! Python3
# find_phone_number_regex.py #
# Finds phone numbers in any text provided using regular expressions. #

import re


def search_phone_number_regex(text):
    '''search_phone_number_regex searches for phone numbers in any given string,
    and printes the result.


    Args:
        text (string): any string to be checked for phone numbers
    '''

    phone_number_regex = re.compile(r'(\d{3}-?\d{3}-\d{4})')
    match_object = phone_number_regex.findall(text)
    print('Phone numbers found: ' + str(match_object))


search_phone_number_regex('Cell: 415-555-9999 Work: 212-555-0000')
