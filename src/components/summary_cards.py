import dash_bootstrap_components as dbc

color='white'

style = {
    'height': 220
}

card_total_acc = dbc.Card(
    color=color,
    style=style,
    id="card-total-acc"
)
card_total_fatal = dbc.Card(
    color=color,
    style=style,
    id="card-total-fatal"
)
card_avg_resp = dbc.Card(
    color=color,
    style=style,
    id="card-avg-resp"
)
card_total_eco_loss = dbc.Card(
    
    color=color,
    style=style,
    id="card-total-eco-loss"
)

card_leading_cause = dbc.Card(
    color=color,
    style=style,
    id="card-leading-cause"
)

summary_cards = dbc.Row([
    dbc.Col(card_total_acc),
    dbc.Col(card_total_fatal),
    dbc.Col(card_avg_resp),
    dbc.Col(card_total_eco_loss),
    dbc.Col(card_leading_cause)
])