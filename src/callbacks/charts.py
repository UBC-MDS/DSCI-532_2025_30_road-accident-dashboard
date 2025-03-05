import altair as alt
from dash import Input, Output, callback, ctx
from constants.constants import GROUP_BY_SEVERITY, GROUP_BY_TIME
from data.canadian_data import canadian_data
from string_resources.en import (
    CHART_GROUP_BY_SEVERITY_LABEL,
    CHART_GROUP_BY_TIME_LABEL,
    CHART_EMERGENCY_RESPONSE_TIME_Y_AXIS_LABEL,
    CHART_ACCIDENT_COUNT_Y_AXIS_LABEL,
)
import functools

alt.data_transformers.enable("vegafusion")


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


def get_emergency_response_time_chart(df, input_category):
    category_label, category_numeric = get_category(input_category)
    chart = (
        alt.Chart(df)
        .mark_boxplot()
        .encode(
            x=alt.X(
                category_numeric,
                title=category_label,
                sort=alt.EncodingSortField(
                    field="Emergency Response Time", op="median", order="descending"
                ),
            ),
            y=alt.Y(
                "Emergency Response Time:Q",
                title=CHART_EMERGENCY_RESPONSE_TIME_Y_AXIS_LABEL,
            ),
            color=alt.Color(category_numeric, legend=None),
            tooltip=[category_numeric, "Emergency Response Time:Q", category_numeric],
        )
        .properties(width=340, height=250)
    )
    return chart


def get_weather_chart(df, input_category):
    _, category_numeric = get_category(input_category)
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Weather Conditions", sort="-y"),
            y=alt.Y(
                "count():Q", axis=alt.Axis(title=CHART_ACCIDENT_COUNT_Y_AXIS_LABEL)
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
            ),
            tooltip=["Weather Conditions", "count():Q", category_numeric],
        )
        .properties(width=330, height=217)
    )
    return chart


def get_age_chart(df, input_category):
    _, category_numeric = get_category(input_category)
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "count():Q", axis=alt.Axis(title=CHART_ACCIDENT_COUNT_Y_AXIS_LABEL)
            ),
            y=alt.Y("Driver Age Group", sort=["61+", "41-60", "26-40", "18-25", "<18"]),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
            ),
            tooltip=["count():Q", "Driver Age Group", category_numeric],
        )
        .properties(width=350, height=238)
    )
    return chart


def get_line_chart(df, input_category):
    category_label, category_numeric = get_category(input_category)
    accident_counts = (
        df.groupby(["Year", category_label]).size().reset_index(name="Accident Count")
    )

    line = (
        alt.Chart(accident_counts)
        .mark_line()
        .encode(
            x="Year:O",
            y="Accident Count:Q",
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
            ),
        )
    )

    points = (
        alt.Chart(accident_counts)
        .mark_point()
        .encode(
            x="Year:O",
            y=alt.Y("Accident Count:Q", title=CHART_ACCIDENT_COUNT_Y_AXIS_LABEL),
            color=alt.Color(category_numeric, legend=None),
            tooltip=["Year:O", "Accident Count:Q", category_numeric],
        )
    )

    chart = (line + points).properties(width=850, height=200)

    return chart

def get_road_chart(df, input_category):
    _, category_numeric = get_category(input_category)
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Road Condition", sort="-y"),
            y=alt.Y(
                "count():Q", axis=alt.Axis(title=CHART_ACCIDENT_COUNT_Y_AXIS_LABEL)
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
            ),
            tooltip=["Road Condition", "count():Q", category_numeric],
        )
        .properties(width=350, height=184)
    )
    return chart


@callback(
    Output("emergency_response_time_chart", "spec"),
    Output("weather_chart", "spec"),
    Output("age_chart", "spec"),
    Output("line_chart", "spec"),
    Output("road_chart", "spec"),
    Output("urban-rural", "value"),
    Output("season", "value"),
    Output("weather-condition", "value"),
    Output("road-condition", "value"),
    Output("time-of-day", "value"),
    Output("year-slider", "value"),
    Output("month-checklist", "value"),
    Output("group_by_radio", "value"),
    Input("group_by_radio", "value"),
    Input("urban-rural", "value"),
    Input("season", "value"),
    Input("weather-condition", "value"),
    Input("road-condition", "value"),
    Input("time-of-day", "value"),
    Input("year-slider", "value"),
    Input("month-checklist", "value"),
)
def load_chart(
    group_by_category,
    urban_rural,
    season,
    weather_condition,
    road_condition,
    time_of_day,
    year_range,
    months,
):
    raw_df = get_data()
    df = filter_data(
        raw_df,
        urban_rural,
        season,
        weather_condition,
        road_condition,
        time_of_day,
        year_range,
        months,
    )
    emergency_response_time_chart = get_emergency_response_time_chart(
        df, group_by_category
    )
    weather_chart = get_weather_chart(df, group_by_category)
    age_chart = get_age_chart(df, group_by_category)
    line_chart = get_line_chart(df, group_by_category)
    road_chart = get_road_chart(df, group_by_category)
    return (
        emergency_response_time_chart.to_dict(format="vega"),
        weather_chart.to_dict(format="vega"),
        age_chart.to_dict(format="vega"),
        line_chart.to_dict(format="vega"),
        road_chart.to_dict(format="vega"),
    )
