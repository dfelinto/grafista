import logging.config
import os
from peewee import SqliteDatabase
from flask import Flask

log = logging.getLogger(__name__)


# App init and configuration
app = Flask(__name__)

# Load configuration from three different sources, to make it easy to override
# settings with secrets, as well as for development & testing.
app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.config.from_pyfile(os.path.join(app_root, 'config.py'), silent=False)
app.config.from_pyfile(os.path.join(app_root, 'config_local.py'), silent=True)

# Configure logging
logging.config.dictConfig(app.config['LOGGING'])
log = logging.getLogger(__name__)
if app.config['DEBUG']:
    log.info('Grafista starting, debug=%s', app.config['DEBUG'])

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
db = SqliteDatabase(app.config['DATABASE'], threadlocals=True)


@app.before_request
def _db_connect():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()


@app.context_processor
def inject_series():
    from application.models import Series
    return dict(series=Series.select())
