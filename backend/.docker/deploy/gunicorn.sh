#!/bin/bash
cd /app/api
#gunicorn openecoe-chrono:app -k eventlet --daemon  --workers 1 --bind=127.0.0.1:5001 --reload -c /app/api/configs/gunicorn_conf.py --capture-output --enable-stdio-inheritance
#gunicorn openecoe-api:app --daemon --bind=unix:/run/ecoe-api.sock --reload -c /app/api/configs/gunicorn_conf.py --capture-output --enable-stdio-inheritance
# 1. Levantar el CHRONO
gunicorn openecoe-chrono:app -k eventlet --workers 1 --bind=0.0.0.0:5002 --capture-output &
# 2. Levantar la API
gunicorn openecoe-api:app --bind=0.0.0.0:5000 --workers 4 --capture-output &
# 3. Levantar el worker de colas
flask rq worker &
# Esperar para que el contenedor no se cierre
wait