from dash import Dash, html
import dash_bootstrap_components as dbc
from components.navbar import navbar, about_text
from components.sidebar import sidebar
from components.summary_cards import summary_cards
from components.charts import emergency_response_time_chart, categorical_chart, age_chart, line_chart
from data.canadian_data import canadian_data
from string_resources.en import APP_MASTER_TITLE
import plotly.express as px
import callbacks # DO NOT DELETE THIS x_x

# App init
data = canadian_data
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = APP_MASTER_TITLE
server = app.server

# App layout
app.layout = dbc.Container([
    dbc.Row([
        navbar,
        about_text,
    ]),
    html.Br(),
    dbc.Row([
        sidebar,
        html.Br(),
        dbc.Col([
            dbc.Row(summary_cards),
            html.Br(),
            dbc.Row([
                dbc.Col(emergency_response_time_chart),
                dbc.Col(categorical_chart),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(age_chart),
                dbc.Col(line_chart),
            ]),
            ], md=9
        )
    ])
])

if __name__ == "__main__":
    app.run(debug=True)