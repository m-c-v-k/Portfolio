# Imporing necessary libraries
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import os

# 10

# Test / example - stacked bar
country = {
    "name": ["SWE", "FIN", "NOR", "DEN", "ISL"],
    "gold": [5, 7, 8, 3, 2],
    "silver": [8, 4, 6, 4, 1],
    "bronze": [10, 11, 5, 3, 0]
}

df = pd.DataFrame(country)

fig = go.Figure(
    data=[
        go.Bar(name='Gold', x=df['name'], y=df['gold']),
        go.Bar(name='Silver', x=df['name'], y=df['silver']),
        go.Bar(name='Bronze', x=df['name'], y=df['bronze'])
    ]
)

fig.update_layout(barmode='stack')
fig.show()

# 10.a

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_path = f'{CURR_DIR_PATH}/../D1/data/London 2012 Olympic alternative medal rankings - ALL.csv'

df = pd.read_csv(data_path)
df.sort_values('Total', ascending=False, na_position='last', inplace=True)
df = df.head(10)

print(df)
fig = go.Figure(
    data=[
        go.Bar(name='Gold', x=df['Gold'], y=df['ISO'], orientation='h'),
        go.Bar(name='Silver', x=df['Silver'], y=df['ISO'], orientation='h'),
        go.Bar(name='Bronze', x=df['Bronze'], y=df['ISO'], orientation='h')
    ]
)

fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total ascending'})
fig.show()
