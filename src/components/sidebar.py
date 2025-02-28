import dash_bootstrap_components as dbc
from dash import html, dcc
from constants.constants import GROUP_BY_SEVERITY, GROUP_BY_TIME
from string_resources.en import (
    SIDEBAR_TITLE,
    SIDEBAR_GROUP_BY_LABEL,
    SIDEBAR_GROUP_BY_OPTION_SEVERITY,
    SIDEBAR_GROUP_BY_OPTION_TIME,
)

from data.canadian_data import canadian_data


def get_unique(col_name):
    return canadian_data[col_name].unique()


group_by_radio = dcc.RadioItems(
    options=[
        {"label": SIDEBAR_GROUP_BY_OPTION_SEVERITY, "value": GROUP_BY_SEVERITY},
        {"label": SIDEBAR_GROUP_BY_OPTION_TIME, "value": GROUP_BY_TIME},
    ],
    value=GROUP_BY_SEVERITY,  # default is by severity
    id="group_by_radio",
    inline=True,
    className="custom-radio-items",
)

# TODO: TO BE EDITED BY FRANKLIN HERE
sidebar = dbc.Col(
    [
        html.H4(SIDEBAR_TITLE),
        html.Br(),
        html.H6(SIDEBAR_GROUP_BY_LABEL),
        group_by_radio,
        html.Br(),
        dcc.Dropdown(
            id="urban-rural-dropdown",
            options=[{"label": r, "value": r} for r in get_unique("Urban/Rural")],
            multi=True,
            placeholder="Select multiple settlement types",
        ),
        html.Br(),
        dcc.Dropdown(),
        html.Br(),
        dcc.Dropdown(),
        html.Br(),
        dcc.Dropdown(),
        html.Br(),
        dcc.Dropdown(),
    ],
    # md=3,
    style={"background-color": "#e6e6e6", "padding": 15, "border-radius": 3},
)
