#! Python3

# A walkthrough of section 6 and 7 in 'The Python Bible' course

### Section 6 - If THIS, then That: Logic and Conditional Flow in Python ###

# 6.31
'''
print(2 > 3)
print(2 < 3)
print(type(2 < 3))
print(2 == 3)
print(3 == 3)
print(2 != 3)
print(4 >= 3)
print(3 >= 3)
print(4 <= 3)
'''
# 6.32
'''
if True:
    print("It worked!")

num1 = 100
num2 = 150

if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bigger than num1")
else:
    print("Both numbers are equal")
'''
# 6.33
'''
print(not True)
print(not False)
print(not 2 < 3)
print(not 4 == 3)

x = 10
y = 20
if not y > x:
    print("It worked")

c = 10
d = 5

if c > 10 and d > 1:
    print("It worked")

if c >= 10 and d > 1:
    print("It worked")

if not (c > 10 and d > 1):
    print("It worked")
'''
# 6.34
'''
c = 5
d = -1

if c > 1 or d > 1:
    print("It worked")

if c > 100 or d > 100:
    print("It worked")

if not (c > 100 or d > 100):
    print("It worked")

c = 6
d = 2

if (c > 5 and d > 5) or (c > 1 and d > 1):
    print("It worked")
'''

### Section 7 - Hold This For Me: Python Datastructures ###

# 7.37
