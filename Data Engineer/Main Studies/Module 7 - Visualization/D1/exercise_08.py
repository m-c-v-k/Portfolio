# Imporing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import os

# 8

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_path = f'{CURR_DIR_PATH}/data/forsaljning.csv'

df = pd.read_csv(data_path)

y1 = df['2019']
y2 = df['2020']
y3 = df['2021']

years = pd.concat([y1, y2, y3])
months = list(range(1, 37))


plt.plot(months, years)
plt.show()
plt.close()
