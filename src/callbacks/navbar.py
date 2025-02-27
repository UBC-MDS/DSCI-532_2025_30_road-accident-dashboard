from dash import Input, Output, State, callback

@callback(
    Output("about-text", "style"),
    Input("open-about", "n_clicks"),
    State("about-text", "style"),
)
def toggle_about(n, about_style):
    print("I'm clicked ! ! !")
    if n:
        if about_style and about_style.get('display') == 'none':
            about_style['display'] = 'block'  
        else:
            about_style['display'] = 'none'
    return about_style