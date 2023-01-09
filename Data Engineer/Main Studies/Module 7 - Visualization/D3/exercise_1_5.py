#! python3

# Importing necessary libraries
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash import Dash
from dash import Input
from dash import Output
# 1

df = {
    'x0': [-2, -1, 0, 1, 2],
    'y0': [5, 3, -3, 4, 8],
    'y1': [1, 5, 0, -4, 1]
}


def select_df(data):
    x_data = df['x0']
    y_data = df[f'y{data}']

    return x_data, y_data


def select_plot_type(dropdown_type, df_data):
    x_data = df_data[0]
    y_data = df_data[1]
    if dropdown_type == 'line':
        fig = px.line(x=x_data, y=y_data)
    # 4
    elif dropdown_type == 'bar':
        fig = px.bar(x=x_data, y=y_data)
    # 5
    elif dropdown_type == 'scatter':
        fig = px.scatter(x=x_data, y=y_data)

    return fig

# 2


app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown_type',
        options=[
            {'label': 'Line', 'value': 'line'},
            {'label': 'Bar', 'value': 'bar'},
            {'label': 'Scatter', 'value': 'scatter'}
        ],
        value='line'
    ),
    dcc.Dropdown(
        id='dropdown_data',
        options=[
            {'label': 'Original', 'value': 0},
            {'label': 'Changed Y', 'value': 1}
        ],
        value=0
    ),
    dcc.Graph(id='graph_plotly')
])


@app.callback(
    Output(component_id='graph_plotly',
           component_property='figure'),
    [Input(component_id='dropdown_data',
           component_property='value')],
    [Input(component_id='dropdown_type',
           component_property='value')]
)
# 3
def graph_update(dropdown_data, dropdown_type):

    data = select_df(dropdown_data)
    figure = select_plot_type(dropdown_type, data)

    figure.update_layout(
        width=800,
        height=600,
        title=dropdown_data,
        xaxis_title='x-värden',
        yaxis_title='y-värden'
    )

    return figure


app.run_server()
