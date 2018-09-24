import time
import logging
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    app.logger.info('Ive been hit by root!')
    return "[python]Hello, World!\n"

@app.route('/wait')
def wait():
    time.sleep(5)
    app.logger.info('Ive been hit by wait!')
    return "[python]I waited 5 seconds!\n"

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)