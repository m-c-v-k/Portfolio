#! python3

# Importing necessary libraries

import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash
from dash import dcc
from dash import html
from dash import Input
from dash import Output
from dash import ctx

# Getting data
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_path = f'{CURR_DIR_PATH}/godisAB_forsaljning.csv'

df = pd.read_csv(data_path)

# 1


def mat_plot(type, year):
    if type == 'plot':
        plt.plot(df['Manad'], df[f'{year}'])
    elif type == 'bar':
        plt.bar(df['Manad'], df[f'{year}'])

    plt.title(f'Godis AB {year}')
    plt.xlabel('Månader')
    plt.ylabel('Försäljning i kr')
    plt.show()
    plt.close()


# 1.a
mat_plot('plot', '2020')

# 1.b
mat_plot('plot', '2021')

# 1.c
mat_plot('bar', '2020')

# 1.d
mat_plot('bar', '2021')


# 2
def plotly_plot(type, year):
    if type == 'plot':
        fig = px.line(
            df,
            x='Manad',
            y=year,
            labels={
                'Manad': 'Månad',
                year: 'Försäljning i kr'
            },
            title=f'Godis AB {year}')
    elif type == 'bar':
        fig = px.bar(
            df,
            x='Manad',
            y=year,
            labels={
                'Manad': 'Månad',
                year: 'Försäljning i kr'
            },
            title=f'Godis AB {year}')

    fig.show()


# 2.a
plotly_plot('plot', '2020')

# 2.b
plotly_plot('plot', '2021')

# 2.c
plotly_plot('bar', '2020')

# 2.d
plotly_plot('bar', '2021')


# 3


def select_graph(type, year):
    if type == 'line':
        fig = px.line(
            df,
            x='Manad',
            y=year
        )
    elif type == 'bar':
        fig = px.bar(
            df,
            x='Manad',
            y=year
        )

    return fig


app = Dash(__name__)

app.layout = html.Div([
    # 3.a
    dcc.Dropdown(
        id='dropdown_data',
        options=[
            {'label': '2020', 'value': '2020'},
            {'label': '2021', 'value': '2021'}
        ],
        value='2020'
    ),
    # 3.b
    html.Button(id='btn_line', children='Line', n_clicks=0),
    html.Button(id='btn_bar', children='Bar', n_clicks=0),
    dcc.Graph(
        id='graph_plotly'
    )
])

last_triggered_id = 'btn_line'


@app.callback(
    Output(component_id='graph_plotly',
           component_property='figure'),
    [Input(component_id='dropdown_data',
           component_property='value')],
    [Input(component_id='btn_line',
           component_property='n_clicks')],
    [Input(component_id='btn_bar',
           component_property='n_clicks')]

)
def graph_update(dropdown_data, btn_line, btn_bar):
    global last_triggered_id

    if 'btn_line' == ctx.triggered_id:
        last_triggered_id = ctx.triggered_id
        figure = select_graph('line', dropdown_data)
    elif 'btn_bar' == ctx.triggered_id:
        last_triggered_id = ctx.triggered_id
        figure = select_graph('bar', dropdown_data)
    else:
        if 'btn_line' == last_triggered_id:
            figure = select_graph('line', dropdown_data)
        elif 'btn_bar' == last_triggered_id:
            figure = select_graph('bar', dropdown_data)

    figure.update_layout(
        width=800,
        height=600,
        title=f'Godis AB {dropdown_data}',
        xaxis_title='Månader',
        yaxis_title='Försäljning i kr'
    )

    return figure


app.run_server()
