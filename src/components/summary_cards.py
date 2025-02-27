import dash_bootstrap_components as dbc

# TODO: To be edited by Tien!
color='white'

card_1 = dbc.Card(
    color=color,
    style={"height": 200},
    id="card-1"
)

card_2 = dbc.Card(
    color=color,
    style={"height": 200},
    id="card-2"
)

card_3 = dbc.Card(
    color=color,
    style={"height": 200},
    id="card-3"
)

card_4 = dbc.Card(
    color=color,
    style={"height": 200},
    id="card-4"
)

summary_cards = dbc.Row([
    dbc.Col(card_1),
    dbc.Col(card_2),
    dbc.Col(card_3),
    dbc.Col(card_4)
])