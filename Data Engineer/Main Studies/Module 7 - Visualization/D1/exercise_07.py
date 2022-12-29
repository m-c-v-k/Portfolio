# Imporing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# 7

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_path = f'{CURR_DIR_PATH}/data/forsaljning.csv'

df = pd.read_csv(data_path)

# 7.a


def plot_sales(year):
    plt.plot(df['Manad'], df[f'{year}'])
    plt.title('Försäljning 2019')
    plt.xlabel('Månader')
    plt.ylabel('Försäljning i kronor(kr)')
    plt.show()
    plt.close()


plot_sales('2019')
plot_sales('2020')
plot_sales('2021')

plt.plot(df['Manad'], df['2019'], color='blue')
plt.plot(df['Manad'], df['2020'], color='red')
plt.plot(df['Manad'], df['2021'], color='green')
plt.title('Försälning 2019-2022')
plt.xlabel('Månader')
plt.ylabel('Försäljning i kronor(kr)')
plt.legend()
plt.show()
plt.close()

# 7.b


def scatter_sales(year):
    colors = []

    for value in df[f'{year}']:
        if value == np.amax(df[f'{year}']):
            colors.append('g')
        elif value == np.amin(df[f'{year}']):
            colors.append('r')
        else:
            colors.append('b')

    plt.scatter(df['Manad'], df[f'{year}'], color=colors)
    plt.title('Försäljning 2019')
    plt.xlabel('Månader')
    plt.ylabel('Försäljning i kronor(kr)')
    plt.show()
    plt.close()


scatter_sales('2019')
scatter_sales('2020')
scatter_sales('2021')

# 7.c


def bar_sales(year):
    colors = []

    for value in df[f'{year}']:
        if value == np.amax(df[f'{year}']):
            colors.append('g')
        elif value == np.amin(df[f'{year}']):
            colors.append('r')
        else:
            colors.append('b')

    plt.bar(df['Manad'], df[f'{year}'], color=colors)
    plt.title('Försäljning 2019')
    plt.xlabel('Månader')
    plt.ylabel('Försäljning i kronor(kr)')
    plt.show()
    plt.close()


bar_sales('2019')
bar_sales('2020')
bar_sales('2021')

# 7.d
# Bar shows the best stand-alone information for whole months at a smaller interval the plot would have been better
# If a combination is possible a combination of bar and plot would be even better.


def plot_bar_sales(year):
    colors = []

    for value in df[f'{year}']:
        if value == np.amax(df[f'{year}']):
            colors.append('g')
        elif value == np.amin(df[f'{year}']):
            colors.append('r')
        else:
            colors.append('b')

    plt.plot(df['Manad'], df[f'{year}'])

    plt.bar(df['Manad'], df[f'{year}'], color=colors)
    plt.title('Försäljning 2019')
    plt.xlabel('Månader')
    plt.ylabel('Försäljning i kronor(kr)')
    plt.show()
    plt.close()


plot_bar_sales('2019')
plot_bar_sales('2020')
plot_bar_sales('2021')
