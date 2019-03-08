"""
This script runs the Demo application using a development server.
"""
from os import environ
from down_read.App import app


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.debug = False
    app.run(host='0.0.0.0', port=PORT)
