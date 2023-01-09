#! python3

# Importing necessary libraries
import plotly.express as pe
import dash
from dash import dcc
from dash import html

# Example code

x_val = [-2, -1, 0, 1, 2]
y_val = [5, 3, -3, 4, 8]

fig = pe.line(x=x_val, y=y_val)

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server()
