import altair as alt
from dash import Input, Output, callback, ctx
from constants.constants import GROUP_BY_SEVERITY, GROUP_BY_TIME, GROUP_BY_SETTLEMENT_TYPE, GROUP_BY_SEASON
from data.canadian_data import canadian_data
from string_resources.en import (
    CHART_GROUP_BY_SEVERITY_LABEL,
    CHART_GROUP_BY_TIME_LABEL,
    CHART_EMERGENCY_RESPONSE_TIME_Y_AXIS_LABEL,
    CHART_ACCIDENT_COUNT_Y_AXIS_LABEL,
    CHART_GROUP_BY_SETTLEMENT_TYPE,
    CHART_GROUP_BY_SEASON
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
        df = df[df["Settlement Type"].isin(urban_rural)]
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
        return CHART_GROUP_BY_SEVERITY_LABEL, "Accident Severity:N", ["Minor", "Moderate", "Severe"]
    elif input_category == GROUP_BY_TIME:
        return CHART_GROUP_BY_TIME_LABEL, "Time of Day:N", ["Morning", "Afternoon", "Evening", "Night"]
    elif input_category == GROUP_BY_SETTLEMENT_TYPE:
        return CHART_GROUP_BY_SETTLEMENT_TYPE, "Settlement Type", ["Urban", "Rural"]
    elif input_category == GROUP_BY_SEASON:
        return CHART_GROUP_BY_SEASON, "Season", ["Spring", "Summer", "Autumn", "Winter"]
    else:
        return None, None, None


def get_emergency_response_time_chart(df, input_category):
    category_label, category_numeric, category_order = get_category(input_category)
    df['Emergency Response Time'] = df['Emergency Response Time'].round(2)
    chart = (
        alt.Chart(df)
        .mark_boxplot()
        .encode(
            x=alt.X(
                category_numeric,
                title=category_label,
                sort=category_order,
                axis=alt.Axis(labelAngle=-360, titlePadding=10)
            ),
            y=alt.Y(
                "Emergency Response Time:Q",
                title=CHART_EMERGENCY_RESPONSE_TIME_Y_AXIS_LABEL,
                axis=alt.Axis(labelAngle=-360, titlePadding=10)
            ),
            color=alt.Color(category_numeric, legend=None),
            tooltip=[
                alt.Tooltip(category_numeric), 
                alt.Tooltip('Emergency Response Time:Q')
            ]
        )
    ).properties(width=330, height=250)

    return chart


def get_weather_chart(df, input_category, count_type):
    category_label, category_numeric, category_order= get_category(input_category)
    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [value for value in category_order if value in filtered_values]
    stacked_type = "normalize" if count_type == 'Normalized' else 'zero'
    count_axis_title = f"{count_type} "+CHART_ACCIDENT_COUNT_Y_AXIS_LABEL

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Weather Conditions", sort="-y",  axis=alt.Axis(labelAngle=-360, titlePadding=10)),
            y=alt.Y(
                "count():Q", 
                axis=alt.Axis(title=count_axis_title,  labelAngle=-360, titlePadding=10),
                stack=stacked_type
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
                scale=alt.Scale(domain=dynamic_order)
            ),
            tooltip=["Weather Conditions", "count():Q", category_numeric],
        )
        .properties(width=300, height=217)
    )
    return chart


def get_age_chart(df, input_category, count_type):
    category_label, category_numeric, category_order= get_category(input_category)
    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [value for value in category_order if value in filtered_values]
    stacked_type = "normalize" if count_type == 'Normalized' else 'zero'
    count_axis_title = f"{count_type} "+CHART_ACCIDENT_COUNT_Y_AXIS_LABEL

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "count():Q", 
                axis=alt.Axis(title=count_axis_title, labelAngle=-360, titlePadding=10),
                stack=stacked_type
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
                scale=alt.Scale(domain=dynamic_order)
            ),
            tooltip=["count():Q", "Driver Age Group", category_numeric],
        )
        .properties(width=340, height=205)
    )
    return chart


def get_line_chart(df, input_category):
    category_label, category_numeric, category_order = get_category(input_category)
    accident_counts = (
        df.groupby(["Year", category_label]).size().reset_index(name="Accident Count")
    )

    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [value for value in category_order if value in filtered_values]

    line = (
        alt.Chart(accident_counts)
        .mark_line()
        .encode(
            x=alt.X("Year:O", axis=alt.Axis(labelAngle=-360,  titlePadding=10)),
            y=alt.Y("Accident Count:Q",  axis=alt.Axis(titlePadding=10)).scale(zero=False),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
                scale=alt.Scale(domain=dynamic_order)
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


def get_road_chart(df, input_category, count_type):
    category_label, category_numeric, category_order= get_category(input_category)
    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [value for value in category_order if value in filtered_values]
    stacked_type = "normalize" if count_type == 'Normalized' else 'zero'
    count_axis_title = f"{count_type} "+CHART_ACCIDENT_COUNT_Y_AXIS_LABEL
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Road Condition", sort="-y", axis=alt.Axis(labelAngle=-360,  titlePadding=10)),
            y=alt.Y(
                "count():Q", 
                axis=alt.Axis(title=count_axis_title),
                stack=stacked_type
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
                scale=alt.Scale(domain=dynamic_order)
            ),
            tooltip=["Road Condition", "count():Q", category_numeric],
        )
        .properties(width=300, height=217)
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
    Output("count_type_radio", "value"),
    Input("group_by_radio", "value"),
    Input("count_type_radio", "value"),
    Input("urban-rural", "value"),
    Input("season", "value"),
    Input("weather-condition", "value"),
    Input("road-condition", "value"),
    Input("time-of-day", "value"),
    Input("year-slider", "value"),
    Input("month-checklist", "value"),
    Input("reset-button", "n_clicks"),
)
def load_chart(
    group_by_category,
    count_type,
    urban_rural,
    season,
    weather_condition,
    road_condition,
    time_of_day,
    year_range,
    months,
    reset_clicks,
):
    min_year, max_year = canadian_data.Year.min(), canadian_data.Year.max()

    # Check if Reset Button was clicked
    if ctx.triggered_id == "reset-button":
        # print("Reset triggered!")
        urban_rural = []
        season = []
        weather_condition = []
        road_condition = []
        time_of_day = []
        year_range = [min_year, max_year]
        months = []
        group_by_category = GROUP_BY_SEVERITY
        count_type = "Raw"

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

    def chart_to_dict(df):
        return (
            get_emergency_response_time_chart(df, group_by_category).to_dict(
                format="vega"
            ),
            get_weather_chart(df, group_by_category, count_type).to_dict(format="vega"),
            get_age_chart(df, group_by_category, count_type).to_dict(format="vega"),
            get_line_chart(df, group_by_category).to_dict(format="vega"),
            get_road_chart(df, group_by_category, count_type).to_dict(format="vega"),
        )

    charts = chart_to_dict(df)

    filters = [
        urban_rural,
        season,
        weather_condition,
        road_condition,
        time_of_day,
        year_range,
        months,
        group_by_category,
        count_type,
    ]

    return (*charts, *filters)
