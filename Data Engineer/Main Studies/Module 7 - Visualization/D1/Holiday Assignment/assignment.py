#! python3

# Importing necessary libraries
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_path = f'{CURR_DIR_PATH}/fiskAB.csv'

df = pd.read_csv(data_path)

# 1 Matplotlib


def sales_plot(year):
    plt.plot(df['Manad'], df[f'{year}'])
    plt.title(f'Fisk AB {year}')
    plt.xlabel('Månader')
    plt.ylabel('Försäljning i kr')
    plt.show()
    plt.close()


def sales_bar(year):
    plt.bar(df['Manad'], df[f'{year}'])
    plt.title(f'Fisk AB {year}')
    plt.xlabel('Månader')
    plt.ylabel('Försäljning i kr')
    plt.show()
    plt.close()


# 1.a
sales_plot('2021')

# 1.b
sales_plot('2022')

# 1.c
sales_bar('2021')

# 1.d
sales_bar('2022')

# 2 Plotly


def sales_plotly_plot(year):
    fig = px.line(df, x=df['Manad'], y=df[f'{year}'], title=f'Fisk AB {year}')
    fig.show()


def sales_plotly_bar(year):
    fig = px.bar(df, x=df['Manad'], y=df[f'{year}'], title=f'Fisk AB {year}')
    fig.show()


# 2.e
sales_plotly_plot('2021')

# 2.f
sales_plotly_plot('2022')

# 2.g
sales_plotly_bar('2021')

# 2.h
sales_plotly_bar('2022')
