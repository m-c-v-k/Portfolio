#! python3

# Importing necessary libraries
import pandas as pd
import os

# Getting current path
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Read data from .csv-file
df = pd.read_csv(f'{CURR_DIR_PATH}/horsie.csv')

# Remove NaN-values
df.fillna('horse', inplace=True)

# Calculate total weight and remove old weight columns
df['weight'] = df['hoof_weight'] + df['rest_of_horse_weight']
df = df.drop(['hoof_weight', 'rest_of_horse_weight'], axis=1)

# Write to .json-file
df.to_json(f'{CURR_DIR_PATH}/horsie.json', orient='records')
print(df)
