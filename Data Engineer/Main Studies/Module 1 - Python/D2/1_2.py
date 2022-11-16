#! Python3

# Importing necessary libraries
import random
import numpy as np
# 1a
print(2 + 4**5)

# 1ab
print(random.randint(0, 10))

# 2a
a = "42 "
output = (a * 5)
print(output[:-1])
print(("42" + " ") * 4 + "42")
print(np.repeat(42, 5))

# 2b
parrot = 15 / 2 + 3
print(parrot)

# 3a
y = 350 * (1 - 0.5)**9
print(y)


# 3b
y = 750 * (1 - 0.5)**10
print(y)

# 4
print((np.random.random()) * 525)
