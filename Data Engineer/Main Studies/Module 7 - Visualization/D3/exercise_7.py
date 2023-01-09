#! python3

# Importing necessary libraries
import plotly.express as px
import pandas as pd
import os
from dash import Dash
from dash import dcc
from dash import html
from dash import Input
from dash import Output

# 7

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_path = f'{CURR_DIR_PATH}/../D1/data/forsaljning.csv'

df = pd.read_csv(data_path)


def select_data(year):
    data_year = df[f'{year}']

    return data_year


def select_plot_type(type, data):
    print('test')
    df['']
    fig = px.type(x=df['Manad'])
