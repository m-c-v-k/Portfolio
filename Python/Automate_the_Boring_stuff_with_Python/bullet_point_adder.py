#! python3
### bullet_point_adder.py ###
### Adds Wolopedia bullet points to the start of each line in the clipboard. ###

import pyperclip

text = pyperclip.paste()

# Seperate lines and add stars

lines = text.split('\n')

for i in range(len(lines)):     # Loop throught ass indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # Add star to each string in 'lines' list

text = '\n'.join(lines)

pyperclip.copy(text)
