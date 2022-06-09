#! Python3
# find_phone_number_regex.py #
# Finds phone numbers in any text provided using regular expressions. #

def search_phone_number_regex(text):
    '''search_phone_number_regex searches for phone numbers in any given string,
    and printes the result.


    Args:
        text (string): any string to be checked for phone numbers
    '''

    phone_number_regex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
    match_object = phone_number_regex.search(text)
    print("Phone numer found: " + match_object.group())


search_phone_number_regex('My number is 415-666-4242.')
