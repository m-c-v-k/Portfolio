#! Python3

# A walkthrough of section 8 and 9 in 'The Python Bible' course

### Section 8 - Going Loopy - Loops in Python ###

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

### Section 9 - Getting Funky - Functions in Python ###

# 9.57
'''
def add(x, y):
    z = x + y
    return z


answer = add(3, 17)
print(answer)


def reverser(iter):

    return iter[::-1]


print_me = reverser("This is my string")
print(print_me)
'''
# 9.58
'''
a = 250


def f1():
    b = a + 10
    print(b)


def f2():
    a = 50
    print(a)


f1()
f2()
print(a)
'''
# 9.59
'''
a = 250


def f1():
    global a
    a = 100
    print(a)


def f2():
    a = 50
    print(a)


f1()
f2()
print(a)

a = [1, 2, 3]


def f1():
    a[0] = 5
    print(a)


def f2():
    a = 50
    print(a)


f1()
f2()
print(a)
'''
# 9.60
'''

def about(name, age, likes="Python"):
    sentence = f"Meet {name}! They are {age} old and they like {likes}."
    return sentence


print(about("jack", 27))
'''
