import altair as alt
import pandas as pd
from dash import Input, Output, callback
from data.canadian_data import canadian_data
import functools

# load data for charts
@functools.lru_cache()
def get_data():
    return canadian_data

# empty charts for when it is empty, this is placeholder
def empty_chart():
    return alt.Chart(pd.DataFrame()).mark_line().encode()

def get_line_chart(df):
    accident_counts = df.groupby(['Year', 'Accident Severity']).size().reset_index(name='Accident Count')
    chart = alt.Chart(accident_counts).mark_line().encode(
        x='Year:O',  # 'O' for ordinal (categorical)
        y='Accident Count:Q',  # 'Q' for quantitative (numerical)
        color='Accident Severity:N',  # 'N' for nominal (categorical)
        tooltip=['Year', 'Accident Severity', 'Accident Count'])
    return chart

@callback(
    Output('emergency_response_time_chart', 'spec'),
    Output('categorical_chart', 'spec'),
    Output('age_chart', 'spec'),
    Output('line_chart', 'spec'),
    Input('load_data', 'value'),
)
def load_chart(load):
    if load:
        df = get_data()
        line_chart = get_line_chart(df)
        return None, None, None, line_chart.to_dict()
    else:
        return empty_chart().to_dict(), empty_chart().to_dict(), empty_chart().to_dict(), empty_chart().to_dict()