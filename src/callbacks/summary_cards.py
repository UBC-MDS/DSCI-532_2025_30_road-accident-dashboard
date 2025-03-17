from dash import Input, Output, State, callback, ctx, html
import dash_bootstrap_components as dbc
from data.canadian_data import canadian_data


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


def generate_card_body(
    title, desc_value, subtitle=" ", subtitle_style=None, tooltip_desc=None
):
    # Split title into two parts; if there's only one word, s2 remains empty.
    words = title.split(" ", 1)
    s1, s2 = words if len(words) == 2 else (title, "")
    tooltip_id = (f"{s1}-{s2}-tooltip").lower()  # e.g., 'total-accidents-tooltip'
    return dbc.Card(
        [
            dbc.CardHeader(
                html.Div(
                    [
                        html.Span(f"{s1} {s2}"),
                        html.Abbr(
                            "\u2753",
                            title=tooltip_desc,
                            style={
                                "cursor": "pointer",
                                "marginLeft": "5px",
                                "color": "blue",
                            },
                        ),
                    ],
                    style={"textAlign": "center"},
                ),
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
            (
                dbc.Tooltip(
                    tooltip_desc,
                    target=tooltip_id,
                    placement="top",
                    delay={"show": 0, "hide": 0},
                )
                if tooltip_desc
                else None
            ),
        ],
        className="card-shadow",
    )


def format_currency(value):
    """
    Format a number with an appropriate currency suffix.
    """
    if value >= 1_000_000_000:  # Billion
        return f"${value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:  # Million
        return f"${value / 1_000_000:.1f}M"
    elif value >= 1_000:  # Thousand
        return f"${value / 1_000:.1f}K"
    else:
        return f"${value:,.1f}"


def format_tooltip_description(year_range, months):
    """
    Format the year range and months filters for tooltips.
    """
    start_year, end_year = year_range[0], year_range[1]
    yr_text = (
        f"between year {start_year} and year {end_year}"
        if start_year != end_year
        else f"in year {start_year}"
    )
    m_text = ""
    if months and len(months) > 1:
        m_text = "for months [" + ", ".join(months) + "], "
    elif months and len(months) == 1:
        m_text = f"for month {months[0]}, "
    return m_text + yr_text


def register_callbacks(app, cache):
    @cache.memoize()
    def get_cached_data():
        """Load and cache the raw dataset."""
        return canadian_data

    @cache.memoize()
    def compute_summary_stats(
        urban_rural,
        season,
        weather_condition,
        road_condition,
        time_of_day,
        year_range,
        months,
    ):
        """
        Compute summary statistics based on filtered data.
        Convert mutable inputs into tuples for caching consistency.
        """
        urban_rural = tuple(urban_rural or [])
        season = tuple(season or [])
        weather_condition = tuple(weather_condition or [])
        road_condition = tuple(road_condition or [])
        time_of_day = tuple(time_of_day or [])
        months = tuple(months or [])
        year_range = tuple(year_range)

        df = filter_data(
            get_cached_data(),
            urban_rural,
            season,
            weather_condition,
            road_condition,
            time_of_day,
            year_range,
            months,
        )

        total_accidents = len(df)
        total_fatalities = (
            df["Number of Fatalities"].sum() if "Number of Fatalities" in df else 0
        )
        avg_response_time = (
            df["Emergency Response Time"].mean()
            if "Emergency Response Time" in df
            else 0
        )
        total_economic_loss = df["Economic Loss"].sum() if "Economic Loss" in df else 0

        change_accidents = compute_pct_change_earliest_latest(df, None)
        change_fatalities = compute_pct_change_earliest_latest(
            df, "Number of Fatalities", agg="sum"
        )
        change_response_time = compute_pct_change_earliest_latest(
            df, "Emergency Response Time", agg="mean"
        )
        change_economic_loss = compute_pct_change_earliest_latest(
            df, "Economic Loss", agg="sum"
        )

        cause_counts = df["Accident Cause"].value_counts()
        if cause_counts.empty:
            leading_cause = "N/A"
        else:
            top_cause = cause_counts.index[0]
            # If it's a single word, insert line breaks.
            if len(top_cause.split()) == 1:
                leading_cause = html.Span([top_cause, html.Br(), html.Br()])
            else:
                leading_cause = top_cause

        acc_tooltip_desc = (
            "Total Accidents and percentage changes, "
            + format_tooltip_description(year_range, months)
        )
        fat_tooltip_desc = (
            "Total Fatalities and percentage changes, "
            + format_tooltip_description(year_range, months)
        )
        ert_tooltip_desc = (
            "Average Emergency Response Time and percentage changes, "
            + format_tooltip_description(year_range, months)
        )
        eco_tooltip_desc = (
            "Total Economic Loss and percentage changes, "
            + format_tooltip_description(year_range, months)
        )
        cause_tooltip_desc = "Leading cause of accidents " + format_tooltip_description(
            year_range, months
        )

        return {
            "total_accidents": total_accidents,
            "total_fatalities": total_fatalities,
            "avg_response_time": avg_response_time,
            "total_economic_loss": total_economic_loss,
            "change_accidents": change_accidents,
            "change_fatalities": change_fatalities,
            "change_response_time": change_response_time,
            "change_economic_loss": change_economic_loss,
            "leading_cause": leading_cause,
            "total_accidents_tooltip": acc_tooltip_desc,
            "total_fatalities_tooltip": fat_tooltip_desc,
            "avg_response_time_tooltip": ert_tooltip_desc,
            "total_economic_loss_tooltip": eco_tooltip_desc,
            "leading_cause_tooltip": cause_tooltip_desc,
        }

    @callback(
        Output("card-total-acc", "children"),
        Output("card-total-fatal", "children"),
        Output("card-avg-resp", "children"),
        Output("card-total-eco-loss", "children"),
        Output("card-leading-cause", "children"),
        Input("apply-filter", "n_clicks"),
        Input("reset-filter", "n_clicks"),
        State("urban-rural", "value"),
        State("season", "value"),
        State("weather-condition", "value"),
        State("road-condition", "value"),
        State("time-of-day", "value"),
        State("year-slider", "value"),
        State("month-checklist", "value"),
    )
    def load_summary_cards(
        apply_clicks,
        reset_clicks,
        urban_rural,
        season,
        weather_condition,
        road_condition,
        time_of_day,
        year_range,
        months,
    ):
        triggered = ctx.triggered_id
        # If the Reset button is clicked, revert filters to their default values.
        min_year, max_year = get_cached_data().Year.min(), get_cached_data().Year.max()
        if triggered == "reset-filter":
            urban_rural = []
            season = []
            weather_condition = []
            road_condition = []
            time_of_day = []
            year_range = [min_year, max_year]
            months = []
        stats = compute_summary_stats(
            urban_rural,
            season,
            weather_condition,
            road_condition,
            time_of_day,
            year_range,
            months,
        )
        return (
            generate_card_body(
                "Total Accidents",
                f"{stats['total_accidents']:,.0f}",
                stats["change_accidents"][0],
                stats["change_accidents"][1],
                tooltip_desc=stats["total_accidents_tooltip"],
            ),
            generate_card_body(
                "Total Fatalities",
                f"{stats['total_fatalities']:,.0f}",
                stats["change_fatalities"][0],
                stats["change_fatalities"][1],
                tooltip_desc=stats["total_fatalities_tooltip"],
            ),
            generate_card_body(
                "Average ERT",
                f"{stats['avg_response_time']:.1f} min",
                stats["change_response_time"][0],
                stats["change_response_time"][1],
                tooltip_desc=stats["avg_response_time_tooltip"],
            ),
            generate_card_body(
                "Economic Loss",
                format_currency(stats["total_economic_loss"]),
                stats["change_economic_loss"][0],
                stats["change_economic_loss"][1],
                tooltip_desc=stats["total_economic_loss_tooltip"],
            ),
            generate_card_body(
                "Leading Cause",
                stats["leading_cause"],
                tooltip_desc=stats["leading_cause_tooltip"],
            ),
        )
