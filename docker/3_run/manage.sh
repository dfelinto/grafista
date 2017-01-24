#!/usr/bin/env bash -e

. /data/venv/bin/activate
cd /data/git/grafista
python manage.py "$@"
