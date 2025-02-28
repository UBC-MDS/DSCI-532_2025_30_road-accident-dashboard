import altair as alt
import pandas as pd
from dash import Input, Output, callback, html
import dash
import dash_bootstrap_components as dbc
from constants.constants import GROUP_BY_SEVERITY, GROUP_BY_TIME
from data.canadian_data import canadian_data
import functools


# load data for charts
@functools.lru_cache()
def get_data():
    return canadian_data


def filter_data(
    df,
    urban_rural,
    season,
    weather_condition,
    road_condition,
    time_of_day,
    year_range,
    months,
):
    """Filter the data based on sidebar selections."""
    if urban_rural:
        df = df[df["Urban/Rural"].isin(urban_rural)]
    if season:
        df = df[df["Season"].isin(season)]
    if weather_condition:
        df = df[df["Weather Conditions"].isin(weather_condition)]
    if road_condition:
        df = df[df["Road Condition"].isin(road_condition)]
    if time_of_day:
        df = df[df["Time of Day"].isin(time_of_day)]
    if year_range:
        df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]
    if months:
        df = df[df["MonthX"].isin(months)]
    return df



def get_category(input_category):
    # python does not have switch-case SMH
    if input_category == GROUP_BY_SEVERITY:
        return CHART_GROUP_BY_SEVERITY_LABEL, "Accident Severity:N"
    elif input_category == GROUP_BY_TIME:
        return CHART_GROUP_BY_TIME_LABEL, "Time of Day:N"
    else:
        return None, None

def generate_card_body(title, desc_value, color="black"):

    card_body = dbc.CardBody([
        html.P(title),
        html.Br(),
        html.H3(desc_value, style={"text-align": "center", 'color': color}),
    ])

    return card_body

def get_card_total_accidents(df):
    
    total_acc = len(df)
    title = "Total Number of Accidents"
    desc_value = f"{total_acc}" if total_acc else ''
    cardbody = generate_card_body(title=title, desc_value=desc_value)

    return cardbody

def get_card_total_fatalities(df):
    
    total_fatalities = df['Number of Fatalities'].sum()
    title = "Total Fatalities"
    desc_value = f"{total_fatalities} deaths" if total_fatalities else ''
    cardbody = generate_card_body(title=title, desc_value=desc_value)

    return cardbody

def get_card_avg_response_time(df):
    
    avg_response_time = df['Emergency Response Time'].mean()
    title = "Average Emergency Response Time"
    desc_value = f"{avg_response_time.round(1)} minutes" if avg_response_time else ''
    cardbody = generate_card_body(title=title, desc_value=desc_value)

    return cardbody

def get_card_total_economic_loss(df):
    
    total_eco_loss = df['Economic Loss'].sum()
    title = "Total Economic Loss"
    desc_value = f"{total_eco_loss.round(1)} USD" if total_eco_loss else ''
    cardbody = generate_card_body(title=title, desc_value=desc_value)

    return cardbody

def get_card_leading_cause(df):

    leading_cause = df['Accident Cause'].mode()[0]
    title = "Leading Cause of Accident"
    desc_value = f"{leading_cause}" if leading_cause else ''
    cardbody = generate_card_body(title=title, desc_value=desc_value)

    return cardbody

@callback(
    Output('card-total-acc', 'children'),
    Output('card-total-fatal', 'children'),
    Output('card-avg-resp', 'children'),
    Output('card-total-eco-loss', 'children'),
    Output('card-leading-cause', 'children'),
    Input('group_by_radio', 'value')
)
@functools.lru_cache()
def load_summary_cards(group_by_category):

    raw_df = get_data()
    df = filter_data(raw_df)
    card_total_accidents = get_card_total_accidents(df)
    card_total_fatalities = get_card_total_fatalities(df)
    card_avg_response_time = get_card_avg_response_time(df)
    card_total_economic_loss = get_card_total_economic_loss(df)
    card_leading_cause = get_card_leading_cause(df)
    output = (
        card_total_accidents, card_total_fatalities, card_avg_response_time, 
        card_total_economic_loss, card_leading_cause
    )

    return output