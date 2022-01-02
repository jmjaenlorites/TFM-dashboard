# from os import listdir
from sys import path
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import plotly.express as px

from graphs_functions import im_original, im_generated, load_image


def layout():
    return html.Div([

        html.Div([
            html.H3("TransferStyle Results", id="h3-layout_caso"),
        ], style={'display': 'inline-block', 'width': '100%'}),

        html.Div([
            dcc.Graph(
                id='original',
                style={"height": "100%", "width": "100%"},
                figure=im_original,
            ),
        ], style={'display': 'inline-block', 'width': '33%', 'vertical-align': 'top'}),

        html.Div([
            dcc.Graph(
                id='t_s_image',
                style={"height": "100%", "width": "100%"},
                figure=load_image(),
            ),
        ], style={'display': 'inline-block', 'width': '33%', 'vertical-align': 'top'}),

        html.Div([
            dcc.Graph(
                id='generated',
                style={"height": "100%", "width": "100%"},
                figure=im_generated,
            ),

        ], style={'display': 'inline-block', 'width': '33%', 'vertical-align': 'top'}),

        html.Div([
            html.P("Model used"),
            dcc.Dropdown(
                options=[
                    {'label': 'VGC 50', 'value': '0'},
                    {'label': 'Custom encoder from CVAe', 'value': '1'}
                ],
                value='0', id="model",
            )
        ]),

        html.Div([
            html.P("Learning rate"),
            dcc.Slider(id="learning_rate", min=0, max=7, value=7,
                       marks={x: f"{y:.0e}"
                              for x, y in enumerate([0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05])})
        ], style={'display': 'inline-block', 'width': '100%', }),
        html.Div([
            html.P("Style weight"),
            dcc.Slider(id="style_weight", min=-15, max=16, step=1, value=-1,
                       marks={x: f"{10**x:.0e}" for x in range(-15, 17)})
        ], style={'display': 'inline-block', 'width': '100%', }),
        html.Div([
            html.P("Content weight"),
            dcc.Slider(id="content_weight", min=-15, max=16, step=1, value=-10,
                       marks={x: f"{10**x:.0e}" for x in range(-15, 17)})
        ], style={'display': 'inline-block', 'width': '100%', })
    ])
