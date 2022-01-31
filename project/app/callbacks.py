import logging

from dash.dependencies import Input, Output
from app import app

from graphs_functions import load_image

logging.warning("Loading the callbacks")


@app.callback(
    Output('t_s_image', 'figure'),
    Input('learning_rate', 'value'),
    Input('style_weight', 'value'),
    Input('content_weight', 'value'),
    Input('model', 'value'))
def update_mesh_vs_centerline(learning_rate, style_weight, content_weight, model):
    logging.warning("En callback")
    return load_image(learning_rate, style_weight, content_weight, model)
