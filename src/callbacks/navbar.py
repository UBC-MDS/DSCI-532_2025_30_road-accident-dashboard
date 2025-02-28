from dash import Input, Output, State, callback


@callback(
    Output("about-text", "style"),
    Output("custom-navbar", "style"),
    Input("open-about", "n_clicks"),
    State("about-text", "style"),
    State("custom-navbar", "style"),
)
def toggle_about(n, about_style, navbar_style):
    if n:
        if about_style and about_style.get("display") == "none":
            about_style["display"] = "block"
            navbar_style["border-radius"] = "5px 5px 0 0"
        else:
            about_style["display"] = "none"
            navbar_style["border-radius"] = 5
    return about_style, navbar_style
