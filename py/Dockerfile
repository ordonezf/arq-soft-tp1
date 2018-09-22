FROM python:3.6-slim

RUN pip install flask gunicorn

COPY app.py /opt/server/app.py

WORKDIR /opt/server/

# https://docs.docker.com/compose/gettingstarted/
ENTRYPOINT ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:8000"]
