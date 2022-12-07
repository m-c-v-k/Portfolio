#! python3

# Importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ruined_automobile_path = CURR_DIR_PATH + "/ruined_automobile_data-1.csv"
cleaned_automobile_path = CURR_DIR_PATH + "/cleaned_automibile.csv"

df = pd.read_csv(ruined_automobile_path)
print(df.isnull().any())

df = pd.read_csv(
    ruined_automobile_path,
    na_values={
        'company': ['NaN', '?', 'n.a'],
        'body-style': ['NaN', '?', 'n.a'],
        'wheel-base': ['NaN', '?', 'n.a'],
        'num-of-cylinders': ['NaN', '?', 'n.a'],
        'price': ['NaN', '?', 'n.a']
    }
)

df['company'] = df['company'].fillna(-1)
df['body-style'] = df['body-style'].fillna(-1)
df['wheel-base'] = df['wheel-base'].fillna(-1)
df['num-of-cylinders'] = df['num-of-cylinders'].fillna(-1)
df['price'] = df['price'].fillna(-1)

print(df.to_string())
