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
'''
our_list = [27, 46, -5, 17, 99]
print(our_list)
print(type(our_list))
jackson = ["A", "B", "C", "1", "2", "3", "Do", "Rey", "Mi", True, False]
print(jackson[4])
print(jackson[7])
print(jackson[-2])
x = jackson[6]
print(x)
abc = jackson[0:3]
print(abc)
our_list = [1, 2, [3, 4, 5], 6, 7, 8]
print(our_list[2])
print(our_list[2][0])
print(our_list[2][1])
print(our_list[2][2])

our_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(our_table[0])
print(our_table[1])
print(our_table[2])
print(our_table[0][1])
print(our_table[1][2])
print(our_table[2][1])
print(our_table[1][1:])
'''
# 7.41
'''
a = [5, 12, 72, 55, 89]
a = a + [1]
print(a)
a = a + ["BCD"]
print(a)
a = a + list("BCD")
print(a)
a = a + [1, 2, 3]
print(a)
a = a + list(str(123))
print(a)
a = [5, 12, 72, 55, 89]
a = a + [[5, 6, 7, 8]]
print(a)
a.append([10, 11, 12, 13])
print(a)
a = [5, 12, 72, 55, 89]
a = a.append(10)
print(type(a))
a = [5, 12, 72, 55, 89]
a.insert(2, 100)
print(a)
a[0] = 2
print(a)
a = [1, 2, 3]
a.remove(2)
print(a)
'''
# 7.42
