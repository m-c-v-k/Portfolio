#! python3
### find_phone_number.py ###
### Takes a string and checks if it contains any phone numbers. ###

def is_phone_number(text):
    """ Checking if the text is a phone number or not.

    Args:
        text (string): String to be checked if it's a phone number or not.

    Returns:
        boolean: False if not a phone number (US standard), else True if it's a phone number
    """

    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


def find_phone_number(text):
    """ Takes a string and checks if it contains any phone numbers.

    Args:
        text (string): A string to be chacked for any potential phonenumbers. 
    """
    for i in range(len(text)):

        chunk = text[i:i+12]

        if is_phone_number(chunk):
            print('Phone number found: ' + chunk)

    print('Search finished.')


find_phone_number(
    'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
