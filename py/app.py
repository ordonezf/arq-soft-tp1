import time
import logging
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def root():
    app.logger.info('Ive been hit by root!')
    return "[python]Hello, World!\n"

@app.route('/wait')
def wait():
    time.sleep(5)
    app.logger.info('Ive been hit by wait!')
    return "[python]I waited 5 seconds!\n"

@app.route('/intensive')
def intensive():
    app.logger.info('Ive been hit by intensive!')
    end_loop_time = time.time() + 5
    while time.time() < end_loop_time:
        pass
    return "[python]I processed stuff!\n"

@app.route('/static/<path:path>')
def serve_file(path):
    app.logger.info('Returning file:' + path)
    return send_from_directory(app.static_folder, path)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)