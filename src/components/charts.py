from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from string_resources.en import (
    CHART_EMERGENCY_RESPONSE_TIME_LABEL,
    CHART_CATEGORICAL_BY_WEATHER_CONDITION,
    CHART_CATEGORICAL_BY_ROAD_CONDITION,
    CHART_AGE_LABEL,
    CHART_LINE_LABEL,
)

emergency_response_time_chart = dbc.Card(
    children=[
        html.H5(CHART_EMERGENCY_RESPONSE_TIME_LABEL),
        dcc.Loading(children=[dvc.Vega(id="emergency_response_time_chart", spec={})]),
    ],
    body=True,
)

categorical_chart = dbc.Card(
    children=[
        html.H5(CHART_CATEGORICAL_BY_WEATHER_CONDITION),
        dcc.Loading(children=[dvc.Vega(id="weather_chart", spec={})]),
    ],
    body=True,
)

age_chart = dbc.Card(
    children=[
        html.H5(CHART_AGE_LABEL),
        dcc.Loading(children=[dvc.Vega(id="age_chart", spec={})]),
    ],
    body=True,
)

line_chart = dbc.Card(
    children=[
        html.H5(CHART_LINE_LABEL),
        dcc.Loading(children=[dvc.Vega(id="line_chart", spec={})]),
    ],
    body=True,
)
