#! python3

# Importing necessary libraries
import plotly.express as px
from plotly.subplots import make_subplots
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

app = Dash(__name__)

app.layout = html.Div([
    dcc.Checklist(
        id='checklist',
        options=[
            {'label': '2019', 'value': '2019'},
            {'label': '2020', 'value': '2020'},
            {'label': '2021', 'value': '2021'},
        ],
        value=['2019']
    ),
    dcc.Graph(
        id='graph_plotly'
    ),
])


@app.callback(

    Output(component_id='graph_plotly',
           component_property='figure'),
    [Input(component_id='checklist',
           component_property='value')]
)
def graph_update(checkbox_values):
    print(checkbox_values)
    print(len(checkbox_values))

    figure = make_subplots()

    if len(checkbox_values) == 1:
        figure.add_trace(
            px.line(
                x=df['Manad'],
                y=df[checkbox_values[0]]
            )
        )

    elif len(checkbox_values) == 2:
        figure.add_trace(
            px.line(
                x=df['Manad'],
                y=df[checkbox_values[0]]
            )
        )

        figure.add_trace(
            px.line(
                x=df['Manad'],
                y=df[checkbox_values[1]]
            )
        )

    elif len(checkbox_values) == 3:
        figure.add_trace(
            px.line(
                x=df['Manad'],
                y=df[checkbox_values[0]]
            )
        )

        figure.add_trace(
            px.line(
                x=df['Manad'],
                y=df[checkbox_values[1]]
            )
        )

        figure.add_trace(
            px.line(
                x=df['Manad'],
                y=df[checkbox_values[2]]
            )
        )

    # figure = select_plot_type('line', checkbox_values[0])
    # figure = select_plot_type('line', checkbox_values[1])

    figure.update_layout(
        width=800,
        height=600,
        title=f'Försäljning {checkbox_values}',
        xaxis_title='Månad',
        yaxis_title='Försäljning i tkr'
    )

    return figure


app.run_server()
