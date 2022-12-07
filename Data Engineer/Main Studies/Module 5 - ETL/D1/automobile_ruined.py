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
