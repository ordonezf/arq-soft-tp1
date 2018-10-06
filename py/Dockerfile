FROM python:3.6-slim

RUN pip install flask gunicorn

COPY static/ /opt/server/static

COPY app.py /opt/server/app.py

WORKDIR /opt/server/

# https://docs.docker.com/compose/gettingstarted/
ENTRYPOINT ["gunicorn", "-w", "1", "app:app", "-b", "0.0.0.0:8000"]
