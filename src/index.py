import logging

from app import app
from layouts import layout
import os
import callbacks

try:
    port = os.environ["PORT"]
    logging.warning(f"Port: {port}, port type: {type(port)}")
except:
    port = 8050
app.layout = layout()

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=int(port), debug=False)
