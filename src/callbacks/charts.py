import altair as alt
import pandas as pd
from dash import Input, Output, callback
from constants.constants import GROUP_BY_SEVERITY, GROUP_BY_TIME
from data.canadian_data import canadian_data
import functools

alt.data_transformers.enable("vegafusion")

# load data for charts
@functools.lru_cache()
def get_data():
    return canadian_data

# TODO: Add filter here once Franklin is done with the side panel
def filter_data(df):
    return df

def get_emergency_response_time_category(input_category):
    # python does not have switch-case SMH
    if input_category == GROUP_BY_SEVERITY:
        return "Accident Severity", "Accident Severity:N"
    elif input_category == GROUP_BY_TIME:
        return "Time of Day", "Time of Day:N"
    else:
        return None, None

def get_emergency_response_time_chart(df, input_category):
    category_label, category_numeric = get_emergency_response_time_category(input_category)
    chart = alt.Chart(df).mark_boxplot().encode(
        x=alt.X(
        category_numeric, 
        title=category_label, 
        sort=alt.EncodingSortField(
            field='Emergency Response Time',
            op='median',
            order='descending'
        )
    ),
        y=alt.Y('Emergency Response Time:Q', title="Emergency Response Time (minutes)"),
        color=alt.Color(category_numeric, legend=None),
        tooltip=[category_numeric, 'Emergency Response Time:Q', category_numeric],
    ).properties(
        width=300,
        height=250
    )
    return chart

def get_weather_category(input_category):
    # python does not have switch-case SMH
    if input_category == GROUP_BY_SEVERITY:
        return "Accident Severity", "Accident Severity:N"
    elif input_category == GROUP_BY_TIME:
        return "Time of Day", "Time of Day:N"
    else:
        return None, None

def get_weather_chart(df, input_category):
    _, category_numeric = get_weather_category(input_category)
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Weather Conditions', sort='-y'),
        y=alt.Y('count():Q', axis=alt.Axis(title='Accident Count')),
        color=alt.Color(category_numeric,
            legend=alt.Legend(
                orient='none',
                legendY=-50,
                direction='horizontal',
                titleAnchor='middle')),
        tooltip=['Weather Conditions', 'count():Q', category_numeric],
    ).properties(
        width=375,
        height=217
    )
    return chart

def get_age_chart_category(input_category):
    # python does not have switch-case SMH
    if input_category == GROUP_BY_SEVERITY:
        return "Accident Severity", "Accident Severity:N"
    elif input_category == GROUP_BY_TIME:
        return "Time of Day", "Time of Day:N"
    else:
        return None, None

def get_age_chart(df, input_category):
    _, category_numeric = get_age_chart_category(input_category)
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('count():Q', axis=alt.Axis(title='Accident Count')),
        y=alt.Y('Driver Age Group', sort=['61+', '41-60', '26-40', '18-25', '<18']),
        color=alt.Color(category_numeric,
            legend=alt.Legend(
                orient='none',
                legendY=-50,
                direction='horizontal',
                titleAnchor='middle')),
        tooltip=['count():Q', 'Driver Age Group', category_numeric],
    ).properties(
        width=290,
        height=213
    )
    return chart

def get_line_chart_category(input_category):
    # python does not have switch-case SMH
    if input_category == GROUP_BY_SEVERITY:
        return "Accident Severity", "Accident Severity:N"
    elif input_category == GROUP_BY_TIME:
        return "Time of Day", "Time of Day:N"
    else:
        return None, None

def get_line_chart(df, input_category):
    category_label, category_numeric = get_line_chart_category(input_category)
    accident_counts = df.groupby(['Year', category_label]).size().reset_index(name='Accident Count')
    
    line = alt.Chart(accident_counts).mark_line().encode(
        x='Year:O',
        y='Accident Count:Q',
        color=alt.Color(category_numeric,
            legend=alt.Legend(
                orient='none',
                legendY=-50,
                direction='horizontal',
                titleAnchor='middle')),
    )
    
    points = alt.Chart(accident_counts).mark_point().encode(
        x='Year:O',
        y='Accident Count:Q',
        color=alt.Color(category_numeric, legend=None),
        tooltip=['Year:O', 'Accident Count:Q', category_numeric]
    )
    
    chart = (line + points).properties(
        width=400,
        height=200
    )
    
    return chart

@callback(
    Output('emergency_response_time_chart', 'spec'),
    Output('weather_chart', 'spec'),
    Output('age_chart', 'spec'),
    Output('line_chart', 'spec'),
    Input('group_by_radio', 'value'),
)
def load_chart(group_by_category):
    raw_df = get_data()
    df = filter_data(raw_df)
    emergency_response_time_chart = get_emergency_response_time_chart(df, group_by_category)
    weather_chart = get_weather_chart(df, group_by_category)
    age_chart = get_age_chart(df, group_by_category)
    line_chart = get_line_chart(df, group_by_category)
    return emergency_response_time_chart.to_dict(format = "vega"), weather_chart.to_dict(format = "vega"), age_chart.to_dict(format = "vega"), line_chart.to_dict(format = "vega")