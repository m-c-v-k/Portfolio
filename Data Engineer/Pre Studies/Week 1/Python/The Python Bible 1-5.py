#! Python3

# A walktrhough of the first five sections in 'The Python Bible' course

import math

### Section 1 - Course Introduction ###

### Section 2 - Installing Python, Getting Started & A Top Secret Tip ###

# 2.5
'''
print(1+1)
print(105+10)
'''

### Section 3 - Simple Little Boxes - Variables in Python ###

# 3.9
'''
number = 1
print(number)
print(type(number))

number = "hello"
print(number)
print(type(number))
'''
# 3.10
'''
first_number = 1 + 1
second_number = 105 + 10
print(first_number)
print(second_number)

total = first_number + second_number
print(total)
'''

### Section 4 - The 123s - Numbers in Python ###

# 4.13
'''
print(2 + 3)
print(100 - 20)
print(100 + 20 - 80)
print(2 * 2)
print(2 / 4)
print(10 / 5)
print(type(2))
print(type(0.5))
print(5 % 3)
'''
# 4.14
'''
print(2 * 5 - 1)
# B -rackets ()
# O -der
# D -ivision
# M -ultiplication
# A -ddition
# S -ubstraction
print(2 * (5 - 1))
'''
# 4.17
'''
print(round(2.1))
print(round(1.5))
print(math.floor(1.5))
print(math.ceil(2.1))
print(math.pi)
print(math.e)
print(math.sin(math.pi / 2))
print(math.sin(math.pi))
print(math.floor(math.sin(math.pi)))
print(math.cos(0))
print(math.asin(0))
print(math.acos(0))
print(math.hypot(3, 4))
print(math.pow(2, 3))
print(2 ** 3)
print(math.pow(9, 2))
print(9 ** 2)
print(math.exp(2))
print(math.log(math.e))
print(math.log10(1000))
print(math.log2(8))
'''

### Section 5 - The ABCs - How to use Strings to handle text in Python ###

# 5.20
print("Hello")
name = "Marcus"
print(type(name))
message = 'John said to me; "I will see you later".'
long_string = """this
is a long
string"""
print(long_string)
hello = "Hello world!"
print(hello)
