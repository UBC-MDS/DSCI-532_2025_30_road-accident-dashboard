from dash import html
import dash_bootstrap_components as dbc
from constants.constants import (
    PROJECT_GITHUB_LINK
)
from string_resources.en import ( 
    NAVBAR_GITHUB_BUTTON_LABEL, 
    NAVBAR_ABOUT_BUTTON_LABEL, 
    NAVBAR_PROJECT_TITLE
)

about_text_style = {
    'display': 'none',
    'backgroundColor': '#dc3545',
    'color': 'white',
    'padding-left': '50px',
    'padding-top': '10px',
    'padding-bottom': '10px',
    'border-radius': '0 0 5px 5px',
}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                NAVBAR_GITHUB_BUTTON_LABEL, 
                href=PROJECT_GITHUB_LINK, 
                target="_blank",
                style={'border': '0px'}
            )
        ),
        dbc.Button(
            NAVBAR_ABOUT_BUTTON_LABEL, 
            id="open-about", 
            color="secondary", 
            className="ml-2", 
            style={'border': '0px', 'margin-left': '5px'}
        ),
    ],
    brand=NAVBAR_PROJECT_TITLE,
    brand_href="#",
    brand_style={'font-size' : '40px',
                 'margin-left': 50},
    id='custom-navbar', 
    color="danger",  
    dark=True, 
    style={'border-radius': 5, 
           'padding-right': 0},
    fluid=True
)

about_text = html.P(
    ["Road accidents are a major public safety concern, leading to significant loss of life, economic costs, and infrastructural damage. Understanding the factors contributing to accidents—such as weather conditions, vehicle types, and driver behaviors—can help policymakers and city planners design safer road systems. This dashboard provides interactive visualizations to explore Canadian accident trends, analyze accident severity across different regions, and identify key risk factors. By offering data-driven insights, it helps decision-makers implement targeted interventions to improve road safety."],
    id="about-text",
    style=about_text_style  
)