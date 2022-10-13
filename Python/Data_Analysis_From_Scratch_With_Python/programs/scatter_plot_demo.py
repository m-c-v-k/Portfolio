#! Python3

# Simple demo of a scatter plot chart

# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Example random data
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.show()
