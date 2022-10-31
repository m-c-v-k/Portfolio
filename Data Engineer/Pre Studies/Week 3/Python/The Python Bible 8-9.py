#! Python3

# A walkthrough of section 8 and 9 in 'The Python Bible' course

# 8.48
'''
while True:
    print("Do this")

while 2 > 1:
    print("Hello")

while False:
    print("Hello")

number = 1

while number <= 10:

    if number % 2 == 0:
        print(number)
    number += 1

l = []

while len(l) < 3:
    new_name = input("Please inser a name: ").strip().capitalize()
    l.append(new_name)

print("Sprry list is full")
print(l)
'''
# 8.50
'''
for i in range(1, 11):
    print(i)

for letter in "abcd":
    print(letter)

vowels = 0
consonants = 0

for letter in "iuosdhfioyhs0fr9ehdfouwbeugsdoifbgijsdbfuifghbsodihfodskngjbn":
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter == " ":
        pass
    else:
        consonants += 1

print(f"There are {vowels} vowels and {consonants} consonants.")
'''
# 8.51
'''
students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
'''
# 8.52
'''
even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in range(1, 101) if x % 2 == 1]
print(odd_numbers)

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
'''
