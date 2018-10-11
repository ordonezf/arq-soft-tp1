FROM postgres:10.5-alpine

COPY *.csv /data/

COPY init.sql /docker-entrypoint-initdb.d/
