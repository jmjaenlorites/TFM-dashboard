# import dash
# from dash import dcc
# from dash import html
# from dash.dependencies import Input, Output
# from dash_html_components import Label
# import plotly.graph_objs as go
import plotly.express as px
import logging
import numpy as np


def get_w(w):
    r1 = "1e+" if w >= 0 else "1e-"
    r2 = f"0{abs(w)}" if abs(w) < 10 else f"{abs(w)}"
    return r1 + r2


def load_image_given_path(path, title):
    im = np.load(path, allow_pickle=True)
    im = im if len(im.shape) == 3 else im[0, ...]
    fig = px.imshow(im[:, :, 0],
                    title=title,
                    color_continuous_scale="gray"
                    )
    return fig


def get_lr(lr):
    d = {x: f"{y:.0e}" for x, y in enumerate([0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05])}
    return d[lr]


def get_model(model):
    if model == "0":
        return ""
    elif model == "1":
        return "_2"


def load_image(lr=7, style_weight=-1, content_weight=-10, model='0'):
    logging.warning(f"_{get_lr(lr)}_{get_w(style_weight)}_{get_w(content_weight)}")
    try:
        fig = load_image_given_path(
            path=f"./transfer_style_images{get_model(model)}/"
                 f"im_13_{get_lr(lr)}_{get_w(style_weight)}_{get_w(content_weight)}.npy",
            title=f"LR: {get_lr(lr)} | SW: {get_w(style_weight)} | CW: {get_w(content_weight)}")
        return fig
    except FileNotFoundError:
        logging.error(f"Failed to load {get_lr(lr)}_{get_w(style_weight)}_{get_w(content_weight)}")
        return px.imshow(np.zeros((180, 180)),
                         title="FileNotFoundError",
                         color_continuous_scale="gray"
                         )


logging.warning("Cargando im_original")
im_original = load_image_given_path("./im_13.npy", "Original")
logging.warning("Cargando im_generated")
im_generated = load_image_given_path("./im_13_generated.npy", "Generated")
