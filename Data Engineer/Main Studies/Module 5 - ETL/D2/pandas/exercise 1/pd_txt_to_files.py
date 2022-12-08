#! python3

# Importing necessary libraries
import pandas as pd
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
speed_data_path = CURR_DIR_PATH + "/speed_measurements"

speed_data = pd.read_csv(
    speed_data_path + '.txt',
    sep=',',
    header=None,
    encoding='unicode_escape'
)

speed_data.columns = ['speed', 'license_plate', 'color', 'time']

speed_data.to_csv(speed_data_path + '.csv')
speed_data.to_json(speed_data_path + '.json')
speed_data.to_html(speed_data_path + '.html')
