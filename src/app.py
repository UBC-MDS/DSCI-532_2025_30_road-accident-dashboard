from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from pathlib import Path


# Define the relative path
file_path = (
    (Path(__file__)
     .resolve().parent.parent / "data/raw/road_accident_dataset.csv")
)

# Load Data (Read only 100 rows)
df = pd.read_csv(file_path, nrows=100)

# Initialize the app with Bootstrap for styling
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("Road Accident Dashboard"), className="mb-4")),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Settlement Type"),
                        dcc.Dropdown(
                            id="urban-rural-dropdown",
                            options=[
                                {"label": r, "value": r}
                                for r in df["Urban/Rural"].unique()
                            ],
                            multi=True,
                            placeholder="Select multiple settlement types",
                        ),
                    ],
                    width=6,
                ),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Time of Day"),
                        dcc.Dropdown(
                            id="time-dropdown",
                            options=[
                                {"label": t, "value": t}
                                for t in df["Time of Day"].unique()
                            ],
                            multi=True,
                            placeholder="Select multiple time periods",
                        ),
                    ],
                    width=6,
                ),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="accident-graph", style={"height": "1000px"}),
                    width=12
                )
            ]
        ),
    ]
)


@app.callback(
    Output("accident-graph", "figure"),
    Input("urban-rural-dropdown", "value"),
    Input("time-dropdown", "value"),
)
def update_graph(selected_urban_rural, selected_time):
    if not selected_urban_rural:
        selected_urban_rural = df["Urban/Rural"].unique()
    if not selected_time:
        selected_time = df["Time of Day"].unique()

    filtered_df = df[
        df["Urban/Rural"].isin(selected_urban_rural)
        & df["Time of Day"].isin(selected_time)
    ]

    fig = px.bar(
        filtered_df,
        x="Weather Conditions",
        title="Number of Accidents by Weather Conditions",
        labels={
            "count": "Number of Accidents",
        },
        color="Accident Severity",
        height=1000,
    )
    return fig


if __name__ == "__main__":
    app.run(debug=False)
