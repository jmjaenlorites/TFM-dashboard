# TFM-dashboard

This is a visualization tool developed to easily show the results of apply Style Transfer.

Has been developed with Python, using the Dash framework.

To launch it, you can use mount it using docker compose: 

```docker-compose up```

Or launch it directly calling the `src/index.py` script after install all the required packages.

## Scripts detail

At `src/app.py` the Dash application is created. 

At `src/layouts.py` the main layout is defined. That is the application display we see when the app is launched.

At `src/callbacks.py` the callback that makes the sliders works is defined.

At `src/graph_functions.py` there are some functions to plot the images. The callback function also uses this graph functions.
