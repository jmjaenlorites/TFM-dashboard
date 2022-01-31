# from app import app
from layouts import layout
from settings import port, testing
from callbacks import app


app.layout = layout()

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=int(port), debug=testing)
