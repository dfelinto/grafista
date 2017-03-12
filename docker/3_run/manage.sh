#!/usr/bin/env bash

set -e

. /data/venv/bin/activate
cd /data/git/grafista/grafista
python manage.py "$@"
