import altair as alt
import pandas as pd
from dash import Input, Output, State, callback, ctx
from constants.constants import (
    GROUP_BY_SEVERITY,
    GROUP_BY_TIME,
    GROUP_BY_SETTLEMENT_TYPE,
    GROUP_BY_SEASON,
)
from data.canadian_data import canadian_data
from string_resources.en import (
    CHART_GROUP_BY_SEVERITY_LABEL,
    CHART_GROUP_BY_TIME_LABEL,
    CHART_EMERGENCY_RESPONSE_TIME_Y_AXIS_LABEL,
    CHART_ACCIDENT_COUNT_Y_AXIS_LABEL,
    CHART_GROUP_BY_SETTLEMENT_TYPE,
    CHART_GROUP_BY_SEASON,
)

alt.data_transformers.enable("vegafusion")


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
    """Return chart label, Altair encoding, and category order based on grouping."""
    if input_category == GROUP_BY_SEVERITY:
        return (
            CHART_GROUP_BY_SEVERITY_LABEL,
            "Accident Severity:N",
            ["Minor", "Moderate", "Severe"],
        )
    elif input_category == GROUP_BY_TIME:
        return (
            CHART_GROUP_BY_TIME_LABEL,
            "Time of Day:N",
            ["Morning", "Afternoon", "Evening", "Night"],
        )
    elif input_category == GROUP_BY_SETTLEMENT_TYPE:
        return CHART_GROUP_BY_SETTLEMENT_TYPE, "Settlement Type", ["Urban", "Rural"]
    elif input_category == GROUP_BY_SEASON:
        return CHART_GROUP_BY_SEASON, "Season", ["Spring", "Summer", "Autumn", "Winter"]
    else:
        return None, None, None


def get_emergency_response_time_chart(df, input_category):
    """Generate the emergency response time boxplot."""
    category_label, category_numeric, category_order = get_category(input_category)
    df["Emergency Response Time"] = df["Emergency Response Time"].round(2)
    return (
        alt.Chart(df)
        .mark_boxplot()
        .encode(
            x=alt.X(
                category_numeric,
                title=category_label,
                sort=category_order,
                axis=alt.Axis(labelAngle=-360, titlePadding=10),
            ),
            y=alt.Y(
                "Emergency Response Time:Q",
                title=CHART_EMERGENCY_RESPONSE_TIME_Y_AXIS_LABEL,
                axis=alt.Axis(labelAngle=-360, titlePadding=10),
            ),
            color=alt.Color(category_numeric, legend=None),
            tooltip=[category_numeric, "Emergency Response Time:Q"],
        )
        .properties(width=330, height=260)
    )


def get_weather_chart(df, input_category, count_type="zero"):
    """Generate the weather conditions bar chart."""
    category_label, category_numeric, category_order = get_category(input_category)
    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [v for v in category_order if v in filtered_values]
    stacked_type = "normalize" if count_type == "Normalized" else "zero"
    count_axis_title = f"{count_type} {CHART_ACCIDENT_COUNT_Y_AXIS_LABEL}"

    return (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "Weather Conditions",
                sort="-y",
                axis=alt.Axis(labelAngle=-360, titlePadding=10),
            ),
            y=alt.Y(
                "count():Q",
                axis=alt.Axis(title=count_axis_title, labelAngle=-360, titlePadding=10),
                stack=stacked_type,
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
                scale=alt.Scale(domain=dynamic_order),
            ),
            tooltip=["Weather Conditions", "count():Q", category_numeric],
        )
        .properties(width=300, height=217)
    )


def get_age_chart(df, input_category, count_type="zero"):
    """Generate the driver age group bar chart."""
    category_label, category_numeric, category_order = get_category(input_category)
    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [v for v in category_order if v in filtered_values]
    stacked_type = "normalize" if count_type == "Normalized" else "zero"
    count_axis_title = f"{count_type} {CHART_ACCIDENT_COUNT_Y_AXIS_LABEL}"

    return (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "count():Q",
                axis=alt.Axis(title=count_axis_title, labelAngle=-360, titlePadding=10),
                stack=stacked_type,
            ),
            y=alt.Y(
                "Driver Age Group",
                sort=["61+", "41-60", "26-40", "18-25", "<18"],
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
                scale=alt.Scale(domain=dynamic_order),
            ),
            tooltip=["count():Q", "Driver Age Group", category_numeric],
        )
        .properties(width=340, height=205)
    )


def get_line_chart(df, input_category):
    """Generate the accident trend line chart."""
    category_label, category_numeric, category_order = get_category(input_category)
    accident_counts = (
        df.groupby(["Year", category_label]).size().reset_index(name="Accident Count")
    )
    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [v for v in category_order if v in filtered_values]

    line = (
        alt.Chart(accident_counts)
        .mark_line()
        .encode(
            x=alt.X("Year:O", axis=alt.Axis(labelAngle=-360, titlePadding=10)),
            y=alt.Y("Accident Count:Q", axis=alt.Axis(titlePadding=10)).scale(
                zero=False
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendX=650,
                    legendY=-50,
                    offset=0,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
                scale=alt.Scale(domain=dynamic_order),
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

    return (line + points).properties(width=850, height=200)


def get_road_chart(df, input_category, count_type="zero"):
    """Generate the road condition bar chart."""
    category_label, category_numeric, category_order = get_category(input_category)
    filtered_values = df[category_label].unique().tolist()
    dynamic_order = [v for v in category_order if v in filtered_values]
    stacked_type = "normalize" if count_type == "Normalized" else "zero"
    count_axis_title = f"{count_type} {CHART_ACCIDENT_COUNT_Y_AXIS_LABEL}"

    return (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "Road Condition",
                sort="-y",
                axis=alt.Axis(labelAngle=-360, titlePadding=10),
            ),
            y=alt.Y(
                "count():Q", axis=alt.Axis(title=count_axis_title), stack=stacked_type
            ),
            color=alt.Color(
                category_numeric,
                legend=alt.Legend(
                    orient="none",
                    legendY=-50,
                    direction="horizontal",
                    titleAnchor="middle",
                ),
                scale=alt.Scale(domain=dynamic_order),
            ),
            tooltip=["Road Condition", "count():Q", category_numeric],
        )
        .properties(width=300, height=217)
    )


def register_callbacks(app, cache):
    @cache.memoize()
    def get_cached_data():
        """Load and cache the raw dataset."""
        return canadian_data

    @cache.memoize()
    def get_filtered_data(
        urban_rural,
        season,
        weather_condition,
        road_condition,
        time_of_day,
        year_range,
        months,
    ):
        """
        Return a filtered subset of the data from cache,
        based on all user-selected filters.
        """
        urban_rural = tuple(urban_rural or [])
        season = tuple(season or [])
        weather_condition = tuple(weather_condition or [])
        road_condition = tuple(road_condition or [])
        time_of_day = tuple(time_of_day or [])
        months = tuple(months or [])
        year_range = tuple(year_range)

        df_raw = get_cached_data()
        return filter_data(
            df_raw,
            urban_rural,
            season,
            weather_condition,
            road_condition,
            time_of_day,
            year_range,
            months,
        )

    @cache.memoize()
    def get_charts(
        urban_rural,
        season,
        weather_condition,
        road_condition,
        time_of_day,
        year_range,
        months,
        group_by_category,
    ):
        """
        Return the five charts based on the filtered dataset
        and the user-selected group_by_category.
        """
        urban_rural = tuple(urban_rural or [])
        season = tuple(season or [])
        weather_condition = tuple(weather_condition or [])
        road_condition = tuple(road_condition or [])
        time_of_day = tuple(time_of_day or [])
        months = tuple(months or [])
        year_range = tuple(year_range)

        df = get_filtered_data(
            urban_rural,
            season,
            weather_condition,
            road_condition,
            time_of_day,
            year_range,
            months,
        )

        return (
            get_emergency_response_time_chart(df, group_by_category).to_dict(
                format="vega"
            ),
            get_weather_chart(df, group_by_category).to_dict(format="vega"),
            get_age_chart(df, group_by_category).to_dict(format="vega"),
            get_line_chart(df, group_by_category).to_dict(format="vega"),
            get_road_chart(df, group_by_category).to_dict(format="vega"),
        )

    @callback(
        Output("age_chart", "spec", allow_duplicate=True),
        Input("in-memory-store", "data"),
        Input("age_chart_normalize_checkbox", "value"),
        State("group_by_radio", "value"),
        prevent_initial_call=True,
    )
    def reload_age_chart(df_raw, checkbox_value, group_by_category):
        """Reload only the Age chart with the new stacked mode (normalized or raw)."""
        df = pd.DataFrame(df_raw)
        count_type = "Normalized" if checkbox_value else "Raw"
        return get_age_chart(df, group_by_category, count_type).to_dict(format="vega")

    @callback(
        Output("road_chart", "spec", allow_duplicate=True),
        Input("in-memory-store", "data"),
        Input("road_chart_normalize_checkbox", "value"),
        State("group_by_radio", "value"),
        prevent_initial_call=True,
    )
    def reload_road_chart(df_raw, checkbox_value, group_by_category):
        """Reload only the Road chart with the new stacked mode."""
        df = pd.DataFrame(df_raw)
        count_type = "Normalized" if checkbox_value else "Raw"
        return get_road_chart(df, group_by_category, count_type).to_dict(format="vega")

    @callback(
        Output("weather_chart", "spec", allow_duplicate=True),
        Input("in-memory-store", "data"),
        Input("weather_chart_normalize_checkbox", "value"),
        State("group_by_radio", "value"),
        prevent_initial_call=True,
    )
    def reload_weather_chart(df_raw, checkbox_value, group_by_category):
        """Reload only the Weather chart with the new stacked mode."""
        df = pd.DataFrame(df_raw)
        count_type = "Normalized" if checkbox_value else "Raw"
        return get_weather_chart(df, group_by_category, count_type).to_dict(
            format="vega"
        )

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
        Output("age_chart_normalize_checkbox", "value"),
        Output("road_chart_normalize_checkbox", "value"),
        Output("weather_chart_normalize_checkbox", "value"),
        Output("in-memory-store", "data"),
        Input("apply-filter", "n_clicks"),
        Input("reset-filter", "n_clicks"),
        State("group_by_radio", "value"),
        State("urban-rural", "value"),
        State("season", "value"),
        State("weather-condition", "value"),
        State("road-condition", "value"),
        State("time-of-day", "value"),
        State("year-slider", "value"),
        State("month-checklist", "value"),
    )
    def load_chart(
        apply_clicks,
        reset_clicks,
        group_by_category,
        urban_rural,
        season,
        weather_condition,
        road_condition,
        time_of_day,
        year_range,
        months,
    ):
        """
        Main callback that updates all charts and filter components
        when 'Apply' or 'Reset' is clicked.
        """
        triggered = ctx.triggered_id
        min_year, max_year = canadian_data.Year.min(), canadian_data.Year.max()

        if triggered == "reset-filter":
            urban_rural = []
            season = []
            weather_condition = []
            road_condition = []
            time_of_day = []
            year_range = [min_year, max_year]
            months = []
            group_by_category = GROUP_BY_SEVERITY

        # Convert filters to tuples for caching.
        urban_rural = tuple(urban_rural or [])
        season = tuple(season or [])
        weather_condition = tuple(weather_condition or [])
        road_condition = tuple(road_condition or [])
        time_of_day = tuple(time_of_day or [])
        months = tuple(months or [])
        year_range = tuple(year_range)

        # Get the cached charts.
        charts = get_charts(
            urban_rural,
            season,
            weather_condition,
            road_condition,
            time_of_day,
            year_range,
            months,
            group_by_category,
        )

        # Reset in-chart checkboxes to False (raw) each time filters are applied or reset.
        age_chart_normalize_checkbox_state = False
        road_chart_normalize_checkbox_state = False
        weather_chart_normalize_checkbox_state = False

        # Return updated filter states
        filters = (
            urban_rural,
            season,
            weather_condition,
            road_condition,
            time_of_day,
            year_range,
            months,
            group_by_category,
            age_chart_normalize_checkbox_state,
            road_chart_normalize_checkbox_state,
            weather_chart_normalize_checkbox_state,
        )

        # Provide the filtered DataFrame in the dcc.Store component.
        df = get_filtered_data(
            urban_rural,
            season,
            weather_condition,
            road_condition,
            time_of_day,
            year_range,
            months,
        )
        df_store = df.to_dict("records")

        return (*charts, *filters, df_store)
