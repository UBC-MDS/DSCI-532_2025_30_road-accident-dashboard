from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components.navbar import navbar, about_text
from components.sidebar import sidebar
from components.summary_cards import summary_cards
from components.charts import (
    emergency_response_time_chart,
    weather_chart,
    road_condition_chart,
    age_chart,
    line_chart,
)
from data.canadian_data import canadian_data
from string_resources.en import APP_MASTER_TITLE
from flask_caching import Cache
import callbacks  # DO NOT DELETE THIS x_x
from callbacks.summary_cards import (
    register_callbacks as register_summary_callbacks,
)
from callbacks.charts import (
    register_callbacks as register_chart_callbacks,
)

# App init
data = canadian_data
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], prevent_initial_callbacks = True)
app.title = APP_MASTER_TITLE
server = app.server
cache = Cache(server, config={"CACHE_TYPE": "filesystem", "CACHE_DIR": "tmp"})

# App layout
app.layout = dbc.Container(
    [
        dcc.Store(id='in-memory-store', data=None),
        dbc.Row([navbar, about_text]),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(sidebar),
                html.Br(),
                dbc.Col(
                    dcc.Loading(
                        id="loading-container",
                        type="cube",
                        color="#dc3545",
                        fullscreen=False,
                        children=[
                            dbc.Row(summary_cards, justify="around"),
                            html.Br(),
                            dbc.Row(dbc.Col(line_chart)),
                            html.Br(),
                            dbc.Row(
                                [
                                    dbc.Col(emergency_response_time_chart),
                                    dbc.Col(age_chart),
                                ]
                            ),
                            html.Br(),
                            dbc.Row(
                                [
                                    dbc.Col(weather_chart),
                                    dbc.Col(road_condition_chart),
                                ]
                            ),
                        ],
                    ),
                    md=9,
                ),
            ]
        ),
    ]
)

# Call both register_callbacks functions
register_summary_callbacks(app, cache)
register_chart_callbacks(app, cache)

if __name__ == "__main__":
    app.run(debug=False)
