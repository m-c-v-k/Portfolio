#! python3

# Importing necessary libraries
import plotly.express as px
from dash import Dash
from dash import dcc
from dash import html
from dash import Input
from dash import Output

# 6

df = {
    "lander": ["SWE", "ITA", "NOR", "FIN", "GER", "CHI",
               "ESP", "ESP", "SWE", "FIN"],
    "medaljer": ["Guld", "Silver", "Brons", "Brons", "Guld", "Silver", "Guld", "Guld"]
}


def select_data(data):
    fig = px.histogram(df[data])

    return fig


app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown_data',
        options=[
            {'label': 'Länder', 'value': 'lander'},
            {'label': 'Medaljer', 'value': 'medaljer'}
        ],
        value='medaljer'
    ),
    dcc.Graph(
        id='graph_plotly'
    )
])


@app.callback(
    Output(component_id='graph_plotly',
           component_property='figure'),
    [Input(component_id='dropdown_data',
           component_property='value')]
)
def graph_update(dropdown_data):
    figure = select_data(dropdown_data)

    figure.update_layout(
        width=800,
        height=600,
        title=dropdown_data,
        xaxis_title='x-värden',
        yaxis_title='y-värden'
    )

    return figure


app.run_server()
