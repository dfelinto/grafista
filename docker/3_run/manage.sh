#!/usr/bin/env bash -e

. /data/venv/bin/activate
cd /data/git/grafista/grafista
python manage.py "$@"
