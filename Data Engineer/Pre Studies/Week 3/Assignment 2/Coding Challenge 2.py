#! Python3

'''
Coding Challenge 2 - Format text
Write a Python program that formats an imported string according to the following rules. 

If a "_" is prefixed and appended to a word, it will be displayed completely in capital letters 
(for example "_Academy_" would become “ACADEMY”). If a word is enclosed in two "#" it will be 
written in lower case (for example "#Academy#" would become “academy”). A word without formatting 
marks remains as it was typed. The formatting character is neglected during output. 

For example, this string:

"Everyone _said_ that it would not work. Then someone came, #UNAWARE# of what everyone said, and 
just did it.” 

becomes this string:

"Everyone SAID that it would not work. Then someone came, unaware of what everyone said, and just 
did it.” 

Hint 1: You can create a list from a string with the .split() method: 
“hello world”.split(“ “) yields the list [“hello”, “world”] 

Hint 2: Python has the following methods for strings you might find useful: “foo”.endswith(…) and 
“bar”.startswidth(…). 
'''

# Get user input
user_input = input("Enter a string, words prefixed and appended with (the same) '_' or '#' " +
                   "will be formatted: ").strip().split(" ")

# Loop and handle list
for x in range(len(user_input)):
    # Check for '_'
    if user_input[x].startswith('_') and user_input[x].endswith('_'):
        user_input[x] = user_input[x][1:-1].upper()

    # Check for '#'
    elif user_input[x].startswith('#') and user_input[x].endswith('#'):
        user_input[x] = user_input[x][1:-1].lower()

# Join user_input to a new string and print it
output = " ".join(user_input)
print(output)
