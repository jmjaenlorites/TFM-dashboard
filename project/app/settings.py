import os
import logging

try:
    port = os.environ["PORT"]
except KeyError:
    logging.warning("Failed to load environment variable 'PORT'. Setting port as 8050.")
    port = 8050

try:
    testing = bool(os.environ["TESTING"])
except KeyError:
    logging.warning("Failed to load environment variable 'TESTING'. Setting port as False.")
    testing = False
