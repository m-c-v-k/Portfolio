#! Python3

# Project 7 - Part 1 - Pig Latin Translator
# A small program translating words to pig latin

# Get sentence from user
original = input("Please enter a sentence: ").strip().lower()

# Split sentence into words
words = original.split()

# Loop through words and convert to pig latin
pig_words = []

for word in words:

    # If starting with vowel, add "yay"
    if word[0] in "aeiou":
        new_word = word + "yay"
        pig_words.append(new_word)

    # Otherwise add first consonant cluster to end, and add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break

        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]

        new_word = the_rest + cons + "ay"
        pig_words.append(new_word)

# Stick words back together
output = " ".join(pig_words)

# Output the final string
print(output)
