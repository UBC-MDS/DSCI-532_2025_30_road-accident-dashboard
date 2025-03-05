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


# Min and Max for Year slider
min_year, max_year = canadian_data.Year.min(), canadian_data.Year.max()

# Month order
month_order = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

# Get unique months
unique_months = canadian_data.MonthX.unique()

# Sort based on the natural month order
unique_months_sorted = sorted(unique_months, key=month_order.index)

# Create options for the checklist
month_options = [{"label": m, "value": m} for m in unique_months_sorted]

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
sidebar = dbc.Col(
    [
        html.H4(SIDEBAR_TITLE),
        html.Br(),
        html.H6(SIDEBAR_GROUP_BY_LABEL),
        group_by_radio,
        html.Br(),
        html.Label("Settlement Type"),
        dcc.Dropdown(
            id="urban-rural",
            options=[{"label": r, "value": r} for r in get_unique("Urban/Rural")],
            multi=True,
            placeholder="Select one or more...",
        ),
        html.Br(),
        html.Label("Season"),
        dcc.Dropdown(
            id="season",
            options=[{"label": r, "value": r} for r in get_unique("Season")],
            multi=True,
            placeholder="Select one or more...",
        ),
        html.Br(),
        html.Label("Weather Condition"),
        dcc.Dropdown(
            id="weather-condition",
            options=[
                {"label": r, "value": r} for r in get_unique("Weather Conditions")
            ],
            multi=True,
            placeholder="Select one or more...",
        ),
        html.Br(),
        html.Label("Road Condition"),
        dcc.Dropdown(
            id="road-condition",
            options=[{"label": r, "value": r} for r in get_unique("Road Condition")],
            multi=True,
            placeholder="Select one or more...",
        ),
        html.Br(),
        html.Label("Time of day"),
        dcc.Dropdown(
            id="time-of-day",
            options=[{"label": r, "value": r} for r in get_unique("Time of Day")],
            multi=True,
            placeholder="Select one or more...",
        ),
        html.Br(),
        html.Label("Year"),
        dcc.RangeSlider(
            id="year-slider",
            min=min_year,
            max=max_year,
            value=[min_year, max_year],
            step=1,
            marks={year: str(year) for year in range(min_year, max_year + 1, 6)},
            tooltip={"always_visible": True, "placement": "bottom"},
            updatemode="mouseup",
        ),
        html.Br(),
        html.Label("Month"),
        dcc.Checklist(
            id="month-checklist",
            options=[{"label": m, "value": m} for m in unique_months_sorted],
            value=[],
            inline=True,
            className="month-checklist",
        ),
        html.Br(),
        dbc.Button(
            "Reset Filters",
            id="reset-button",
            className="reset-button mt-3",  # Keep Bootstrap spacing class
        )
    ],
    className="h-100",
    style={
        "background-color": "#e6e6e6",
        "padding": 15,
        "border-radius": 3,
    },
)
