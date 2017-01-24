#!/usr/bin/env bash

if [ "$DEV" = "true" ]; then
    echo "Running in development mode"
    cd /data/git/grafista
    bash /manage.sh runserver --host='0.0.0.0'
else
    # Run Apache
    a2enmod rewrite
    /usr/sbin/apache2ctl -D FOREGROUND
fi
