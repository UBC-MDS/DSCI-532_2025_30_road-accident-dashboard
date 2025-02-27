from dash import html, dcc
import dash_bootstrap_components as dbc

line_chart = dbc.Card(children=[html.H5("World Map of Happiness Scores"),
    dcc.Loading(children=[dcc.Graph(id="line-chart", config={'displayModeBar': False})])],
    body=True)