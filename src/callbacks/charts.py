from dash import Input, Output, callback

@callback(
    Output('emergency_response_time_chart', 'spec'),
    Output('categorical_chart', 'spec'),
    Output('age_chart', 'spec'),
    Output('line_chart', 'spec'),
    Input('load_data', 'value'),
)
def load_chart(load):
    if load:
        return None, None, None, None
    else:
        return None, None, None, None