import dash_bootstrap_components as dbc

card_total_acc = dbc.Card(id="card-total-acc", body=True)
card_total_fatal = dbc.Card(id="card-total-fatal", body=True)
card_avg_resp = dbc.Card(id="card-avg-resp", body=True)
card_total_eco_loss = dbc.Card(id="card-total-eco-loss", body=True)
card_leading_cause = dbc.Card(id="card-leading-cause", body=True)

summary_cards = dbc.Row(
    [
        dbc.Col(card_total_acc),
        dbc.Col(card_total_fatal),
        dbc.Col(card_avg_resp),
        dbc.Col(card_total_eco_loss),
        dbc.Col(card_leading_cause),
    ],
    className="g-3",
    justify="around",
    style={"margin": "0px", "padding": "0px"}
)
