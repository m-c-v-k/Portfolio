import pandas as pd
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, ctx
from db_queries.connect_to_db import connect_to_db as connect
from db_queries.select_from_db import select_from_forecast as sf
# v_user = 111
conn = connect.connect_to_db()

s1_cols = 'air_temperature, valid_time'
s1_lim = ['location_id', 52230, 'approved_time', '2023-01-23 10:01:07']
data = sf.select_from_forecast(conn, s1_cols, s1_lim)

data_list = []
for item in data:
    data_list.append([float(item[0]), item[1]])

df_temp = pd.DataFrame(data_list)


app = Dash(__name__)


def select_graph(type):
    if type == 'line':
        fig = px.line(
            df_temp,
            x=1,
            y=0
        )
    elif type == 'bar':
        fig = px.bar(
            df_temp,
            x=1,
            y=0
        )

    return fig


def generate_table(df, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), max_rows))
        ])
    ])


app.layout = html.Div([
    html.H4(children='ETL Mini-project'),
    generate_table(df_temp),
    dcc.Graph(id="graphPlotly"),
    html.Button(id='btn_line',
                children='Line', n_clicks=0),
    html.Button(id='btn_bar', children='Bar', n_clicks=0)
])

last_triggered_id = 'btn_line'


@app.callback(
    Output(component_id='graphPlotly', component_property='figure'),
    [Input(component_id='btn_line',
           component_property='n_clicks')],
    [Input(component_id='btn_bar',
           component_property='n_clicks')]
)
def graph_update(btn_line, btn_bar):
    global last_triggered_id

    if 'btn_line' == ctx.triggered_id:
        last_triggered_id = ctx.triggered_id
        fig = select_graph('line')
    elif 'btn_bar' == ctx.triggered_id:
        last_triggered_id = ctx.triggered_id
        fig = select_graph('bar')
    else:
        if 'btn_line' == last_triggered_id:
            fig = select_graph('line')
        elif 'btn_bar' == last_triggered_id:
            fig = select_graph('bar')

    fig.update_layout(
        font_family="Arial",
        font_size=20,
        title_font_family="Verdana",
        title_font_size=30,
        font_color="#000000",
        title_font_color="#ACACAC",
        width=800,
        height=600,
        title=f"Temperature in Falsterbo",
        title_x=0.5,
        xaxis_title="Date",
        yaxis_title="Temperature in Celcius",
        xaxis=dict(
            tickmode='linear',
            tickangle=45
        )
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
