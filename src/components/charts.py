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


def create_chart_card(title, chart_id):
    return dbc.Card(
        children=[
            html.H5(title),
            dcc.Loading(children=[dvc.Vega(id=chart_id, spec={})]),
        ],
        body=True,
    )

def create_bar_chart_card(title, chart_id):
    return dbc.Card(
        children=[
            html.H5(title),
            dbc.Checkbox(id=f"{chart_id}_normalize_checkbox", label="Normalize Count"),
            dcc.Loading(children=[dvc.Vega(id=chart_id, spec={})]),
        ],
        body=True,
    )

# Create chart components using the function
line_chart = create_chart_card(CHART_LINE_LABEL, "line_chart")
emergency_response_time_chart = create_chart_card(
    CHART_EMERGENCY_RESPONSE_TIME_LABEL, "emergency_response_time_chart"
)
age_chart = create_bar_chart_card(CHART_AGE_LABEL, "age_chart")
weather_chart = create_bar_chart_card(
    CHART_CATEGORICAL_BY_WEATHER_CONDITION, "weather_chart"
)
road_condition_chart = create_bar_chart_card(
    CHART_CATEGORICAL_BY_ROAD_CONDITION, "road_chart"
)