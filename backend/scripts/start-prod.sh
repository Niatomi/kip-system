#!/usr/bin/env bash

set -e

DEFAULT_MODULE_NAME=src.__main__

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

DEFAULT_GUNICORN_CONF=/src/docker/gunicorn/gunicorn_conf.py
export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
export WORKER_CLASS=${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}

# Start Gunicorn
python -c 'from src.database import db_url; print(db_url)' 
alembic upgrade head

aerich migrate
gunicorn --forwarded-allow-ips "*" -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
