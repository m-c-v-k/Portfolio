#! Python3

# A simple demo of a horizontal bar chart

# Importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Marcus', 'Olivia', 'Luna', 'Bebisen', 'Miso', 'Daisy')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error,
        align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # Labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast did you go today?')

plt.show()
