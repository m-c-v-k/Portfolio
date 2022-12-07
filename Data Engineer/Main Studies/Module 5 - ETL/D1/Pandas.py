#! python3

# Importing necessary libraries
import pandas as pd
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
automobile_path = CURR_DIR_PATH + "/Automobile_data.csv"
automobile_cleaned_path = CURR_DIR_PATH + "/Automobile_data_cleaned.csv"


automobile_df = pd.read_csv(automobile_path)
print(automobile_df.to_string())

# print(automobile_df.head(5))
# print(automobile_df.tail(5))

automobile_df = pd.read_csv(
    automobile_path,
    na_values={
        'price': ["?", "n.a"],
        'num-of-cylinders': ["?", "n.a"],
        'engine-type': ["?", "n.a"],
        'horsepower': ["?", "n.a"],
        'average-mileage': ["?", "n.a"]
    }
)
print(automobile_df.to_string())
automobile_df.to_csv(automobile_cleaned_path)

"""

df = pd.read_csv(automobile_cleaned_path)

df = df[['company', 'price']][df.price == df['price'].max()]
print(df)


manufracturer = df.groupby('company')
toyata_df = manufracturer.get_group('toyota')
print(toyata_df)
"""
