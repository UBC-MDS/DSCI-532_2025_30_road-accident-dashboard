import dash_bootstrap_components as dbc
from dash import html, dcc
from string_resources.en import SIDEBAR_TITLE

# TODO: TO BE EDITED BY FRANKLIN HERE
sidebar = dbc.Col([
    html.H5(SIDEBAR_TITLE),
    dcc.Checklist(id='load_data', options=[' Load Data']),
    html.Br(),
    dcc.Dropdown(),
    html.Br(),
    dcc.Dropdown(),
    html.Br(),
    dcc.Dropdown(),
    html.Br(),
    dcc.Dropdown(),
    html.Br(),
    dcc.Dropdown(),
    html.Br(),
    dcc.Dropdown(),
    ],
    md=3,
    style={
        'background-color': '#e6e6e6',
        'padding': 15,
        'border-radius': 3
    }
)