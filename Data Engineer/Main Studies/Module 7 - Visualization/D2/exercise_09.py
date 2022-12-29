# Imporing necessary libraries
from plotly.subplots import make_subplots
import plotly.graph_objects as oGraph
import pandas as pd
import os

# 9

figure = make_subplots(rows=1, cols=2)

country = {
    "name": ["SWE", "FIN", "NOR", "DEN", "ISL"],
    "gold": [5, 7, 8, 3, 2],
    "silver": [8, 4, 6, 4, 1],
    "bronze": [10, 11, 5, 3, 0]
}

df = pd.DataFrame(country)

figure.add_trace(
    oGraph.Bar(
        x=df['name'],
        y=df['gold'],
    )
)

figure.add_trace(
    oGraph.Bar(
        x=df['name'],
        y=df['silver']
    )
)

figure.add_trace(
    oGraph.Bar(
        x=df['name'],
        y=df['bronze']
    )
)

figure.update_layout(
    width=800,
    height=600,
    title='Example Subplots'
)

figure.show()
