#! python3
# phone_email_extractor.py #
# Extracts all phonenumbers and e-mail adreses from a copied text #

import re
import pyperclip

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Area code, parenthesis optional
    (\s|-|\.)?                      # Seperator, optional
    (\d{3})                         # First three digits
    (\s|-|\.)?                      # Seperator, optional
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
)''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # Username
    @                   # The @ symbol
    [a-zA-Z0-9._%+-]+   # Domain name
    (\.[a-zA-Z]{2,4})   # Dot something
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_number += ' x' + groups[8]
        matches.append(phone_number)

for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n.join(matches)')
    print("Copied to clipboard.")
    print("\n".join(matches))
else:
    print("No phone numbers or E-mail adresses found.")


### Chapter 8 - Reading and Writing Files ###
