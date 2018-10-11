import time
import logging
import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, send_from_directory, request

app = Flask(__name__, static_folder='static')
engine = create_engine('postgres://roy:fielding@postgres:5432/arqsoft')


@app.route('/')
def root():
    app.logger.info('Ive been hit by root!')
    return "[python] Hello, World!\n"

@app.route('/wait')
def wait():
    time.sleep(5)
    app.logger.info('Ive been hit by wait!')
    return "[python] I waited 5 seconds!\n"

@app.route('/intensive')
def intensive():
    app.logger.info('Ive been hit by intensive!')
    end_loop_time = time.time() + 5
    while time.time() < end_loop_time:
        pass
    return "[python] I processed stuff!\n"

@app.route('/static/<path:path>')
def serve_file(path):
    app.logger.info('Returning file:' + path)
    return send_from_directory(app.static_folder, path)

@app.route('/db/movies/top/<top>', methods=['GET'])
def top_movies(top):
    app.logger.info('[python] Ive been hit by top movies, they want the top %s', top)
    sql = '''
    select
        m.name as "Movie",
        avg(r.rating) as "Avg Rating",
        count(*) as "Reviews"
    from movies m
    join ratings r on r.movie_id = m.id
    group by 1
    having count(*) > 800
    order by 2 desc
    limit {}
    '''
    res = pd.read_sql_query(sql.format(top), engine)
    return res.to_html(index=False)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
