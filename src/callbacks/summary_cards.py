from dash import Input, Output, callback, html
import dash_bootstrap_components as dbc
from data.canadian_data import canadian_data
import functools


@functools.lru_cache()
def get_data():
    """Load the dataset once (cached)."""
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
    """
    Filter the data based on the user's sidebar selections.
    This should be called BEFORE we compute earliest-latest changes,
    so we only compare among the data that remains after filtering.
    """
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


def compute_pct_change_earliest_latest(df, col=None, agg="sum"):
    """
    Compare earliest date vs. latest in the (filtered) dataset.
    """
    if df.empty or "Year" not in df.columns:
        return ("N/A", {})

    # Group by Year only. If no month filter is applied, this includes all months.
    if col is None:
        grouped = df.groupby("Year").size().reset_index(name="Count")
        col = "Count"
    elif agg == "sum":
        grouped = df.groupby("Year")[col].sum().reset_index()
    elif agg == "mean":
        grouped = df.groupby("Year")[col].mean().reset_index()
    else:
        return ("N/A", {})

    grouped = grouped.sort_values("Year")
    # print(grouped)

    if len(grouped) < 2:
        return ("N/A", {})

    first_val = grouped[col].iloc[0]
    last_val = grouped[col].iloc[-1]

    if abs(first_val) < 1e-9:
        return ("N/A", {})

    pct_change = ((last_val - first_val) / abs(first_val)) * 100
    if pct_change > 0:
        return (f"+{pct_change:.1f}%", {"color": "red", "text-align": "center"})
    else:
        return (f"{pct_change:.1f}%", {"color": "green", "text-align": "center"})


def generate_card_body(title, desc_value, subtitle=" ", subtitle_style=None):
    s1, s2 = title.split(
        " "
    )  # assuming that the title is only 2 words e.g "Total Accidents"
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div([s1, html.Br(), s2], style={"textAlign": "center"}),
                className="card-header",
            ),
            dbc.CardBody(
                [
                    html.H5(
                        desc_value,
                        style={"text-align": "center", "font-weight": "bold"},
                    ),
                    html.Div(subtitle, style=subtitle_style),
                ],
                style={"padding": "15px"},
            ),
        ],
        className="card-shadow",
    )


def format_currency(value):
    """
    Format a number with appropriate currency suffix:
    """
    if value >= 1_000_000_000:  # Billion
        return f"${value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:  # Million
        return f"${value / 1_000_000:.1f}M"
    elif value >= 1_000:  # Thousand
        return f"${value / 1_000:.1f}K"
    else:
        return f"${value:,.1f}"


def get_card_total_accidents(df):
    title = "Total Accidents"

    total_acc = len(df)
    desc_value = f"{total_acc:,.0f}"

    change_text, change_style = compute_pct_change_earliest_latest(df, None)

    return generate_card_body(
        title, desc_value, subtitle=change_text, subtitle_style=change_style
    )


def get_card_total_fatalities(df):
    title = "Total Fatalities"
    total_fatalities = df["Number of Fatalities"].sum()
    desc_value = f"{total_fatalities:,.0f}" if total_fatalities else 0

    change_text, change_style = compute_pct_change_earliest_latest(
        df, "Number of Fatalities", agg="sum"
    )

    return generate_card_body(
        title, desc_value, subtitle=change_text, subtitle_style=change_style
    )


def get_card_avg_response_time(df):
    title = "Average ERT"
    avg_response_time = df["Emergency Response Time"].mean() if not df.empty else 0
    desc_value = f"{avg_response_time:.1f} min"

    change_text, change_style = compute_pct_change_earliest_latest(
        df, "Emergency Response Time", agg="mean"
    )

    return generate_card_body(
        title, desc_value, subtitle=change_text, subtitle_style=change_style
    )


def get_card_total_economic_loss(df):
    """Total Economic Loss formatted with K, M, B suffixes."""
    title = "Economic Loss"
    total_eco_loss = df["Economic Loss"].sum() if not df.empty else 0

    desc_value = format_currency(total_eco_loss)

    change_text, change_style = compute_pct_change_earliest_latest(
        df, "Economic Loss", agg="sum"
    )

    return generate_card_body(
        title, desc_value, subtitle=change_text, subtitle_style=change_style
    )


def get_card_leading_cause(df):
    cause_counts = df["Accident Cause"].value_counts()
    if cause_counts.empty:
        return generate_card_body("Leading Cause", "N/A")

    top_cause = cause_counts.index[0]
    # second_cause = cause_counts.index[1] if len(cause_counts) > 1 else None

    title = "Leading Cause"
    # If it's a single word, add a line break
    if len(top_cause.split()) == 1:
        desc_value = html.Span([top_cause, html.Br(), html.Br()])
    else:
        desc_value = top_cause  # Keep it as a normal string
    # subtitle = f"Next: {second_cause}" if second_cause else ""

    return generate_card_body(
        title,
        desc_value,
        # subtitle=subtitle,
        # subtitle_style={"text-align": "center", "fontSize": "14px", "color": "green"},
    )


@callback(
    Output("card-total-acc", "children"),
    Output("card-total-fatal", "children"),
    Output("card-avg-resp", "children"),
    Output("card-total-eco-loss", "children"),
    Output("card-leading-cause", "children"),
    Input("group_by_radio", "value"),
    Input("urban-rural", "value"),
    Input("season", "value"),
    Input("weather-condition", "value"),
    Input("road-condition", "value"),
    Input("time-of-day", "value"),
    Input("year-slider", "value"),
    Input("month-checklist", "value"),
)
def load_summary_cards(
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

    # Build each card
    card_total_accidents = get_card_total_accidents(df)
    card_total_fatalities = get_card_total_fatalities(df)
    card_avg_response_time = get_card_avg_response_time(df)
    card_total_economic_loss = get_card_total_economic_loss(df)
    card_leading_cause = get_card_leading_cause(df)

    return (
        card_total_accidents,
        card_total_fatalities,
        card_avg_response_time,
        card_total_economic_loss,
        card_leading_cause,
    )
