from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.navbar import navbar
from components.sidebar import sidebar
from components.summary_cards import summary_cards
from data.canadian_data import canadian_data
from string_resources.en import APP_MASTER_TITLE
import plotly.express as px

# App init
data = canadian_data
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = APP_MASTER_TITLE
server = app.server

# App layout
app.layout = dbc.Container([
    dbc.Row([
        navbar,
    ]),
    dbc.Row([
        sidebar,
        dbc.Col(
            summary_cards,
            md=9
        )
    ])
])

if __name__ == "__main__":
    app.run(debug=True)