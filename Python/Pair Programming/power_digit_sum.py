#! Python3
import math
"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

num = 2**1000
digit = str(num)

list_of_int = [int(i) for i in digit]
print(sum(list_of_int))

# ['1125899906842624']


sum_num = 0
n = len(digit)

for i in digit:
    sum_num += int(i)


for i in range(n):
    sum_num += int(digit[i])


counter = 0
while counter < n:

    sum_num += int(digit[counter])
    counter += 1


counter = 0
while counter < n:
    if 10**counter < num:
        counter += 1
print(sum_num)

print(sum(my_list))
