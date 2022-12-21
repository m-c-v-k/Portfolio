# Imporing necessary libraries
import matplotlib.pyplot as plt

# 3
temp = {
    'max-temp': [1, 2, 4, 6, 7, 8, 9, 5, 4, 2],
    'date': ['1/12', '2/12', '3/12', '4/12', '5/12', '6/12', '7/12', '8/12', '9/12', '10/12']
}

plt.plot(temp['date'], temp['max-temp'], color='#ff0000', marker='o')
plt.title('Temperatures', color='#acacac')
plt.xlabel('Dates', color='blue')
plt.ylabel('Max temperature')
plt.show()
