#! Python3

# 1a
name = "Marcus Klingborg"
print(name[0] + "." + name[7] + ".")

# 1b
split_name = name.split()
print(split_name[1], split_name[0])

# 1c
for letter in name:
    name = name.replace("a", "l")

for letter in name:
    name = name.replace("o", "k")

print(name)

# 2
sentence = "Convert a sentence into the Robber language"
new_sentence = ""
for letter in sentence:
    if letter in "bcdfghjklmnpqrstvwxyz":
        new_sentence += letter.replace(letter, f"{letter}o{letter}")
    else:
        new_sentence += letter

print(new_sentence)

# 3
word = "hello"
placeholder = ["_", "_", "_", "_", "_"]
attempts = 0

while True:
    guess = input("Guess a character: ").lower()
    attempts += 1
    if guess in word:
        count = 0
        for letter in word:
            if letter == guess:
                placeholder[count] = guess
            count += 1
        print(f"Correct, current word {''.join(placeholder)}")
    else:
        print(f"Wrong, currrent word {''.join(placeholder)}")

    if "_" not in placeholder:
        print("You won the game!")
        break
    elif attempts == 10:
        print("You lost the game!")
        break
