import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    print('Ive been hit by root!')
    return "[python]Hello, World!\n"

@app.route('/wait')
def wait():
    time.sleep(5)
    print('Ive been hit by wait!')
    return "[python]I waited 5 seconds!\n"