import logging
from peewee import SqliteDatabase
from flask import Flask
import config

log = logging.getLogger(__name__)


# App init and configuration
app = Flask(__name__)
app.config.from_object(config.Config)
try:
    import config_local
    app.config.from_object(config_local.Config)
except ImportError:
    config_local = None

db = SqliteDatabase(app.config['DATABASE'], threadlocals=True)


@app.before_request
def _db_connect():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()
