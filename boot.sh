#!/bin/bash

flask db init
flask db migrate
flask db upgrade
gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:8080 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level debug