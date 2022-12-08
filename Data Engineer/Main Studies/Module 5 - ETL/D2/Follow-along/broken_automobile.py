#! python3

# Importing necessary libraries
import numpy as np
import pandas as pd
import os
import matplotlib as plt


CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
df_path = CURR_DIR_PATH + "/ruined_automobile_data-1.csv"

df = pd.read_csv(df_path)

acceptable_body_styles = ['sedan', 'hatchback',
                          'wagom', 'hardtop', 'convertible']

print(df[df['body-style'].isin(acceptable_body_styles)])
