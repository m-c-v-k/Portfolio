# Imporing necessary libraries
from plotly.subplots import make_subplots
import plotly.graph_objects as oGraph
import pandas as pd
import os

# 10

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_path = f'{CURR_DIR_PATH}/../D1/data/forsaljning.csv'

df = pd.read_csv(data_path)
