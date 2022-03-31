
import dash
import dash_core_components as dcc
from dash import html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import time
import random
from dash.dependencies import Input, Output

fig2 = go.Figure()

app = dash.Dash()

df = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
)

fig = px.scatter(
    df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

#fig2.add_trace(go.Indicator(value = 200,gauge = {'axis': {'visible': False}},domain = {'row': 0, 'column': 0}))
fig2 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 450,
    title = {'text': "Speed"},
    domain = {'x': [0, 0.5], 'y': [0, 0.5]}
))




app.layout = html.Div([
                        html.Div(id="updatingtext"),
                        html.H1('HAPPY Robot Status Indicator',style={'font-family': 'Helvetica',"margin-top": "25","margin-bottom": "0"},className='eight columns'),
                        dcc.Graph(id="lpower", figure=fig2),
                        dcc.Graph(id="life-exp-vs-gdp", figure=fig),
                        dcc.Interval(id='interval-component',interval=1*1000, n_intervals=0)
                        ])

@app.callback(Output('live-updatingtext-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    speed=0
    speed = random.randint(0,500)
    return [
        html.Span('Longitude: {0:.2f}'.format(speed), style={'font-family': 'Helvetica',"margin-top": "25","margin-bottom": "0"}),
    ]

if __name__ == "__main__":
    #app.run_server(port=8080, host='172.17.21.145',debug=True)
    app.run_server(port=8080,debug=True)

