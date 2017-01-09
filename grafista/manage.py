import logging
import requests
from flask import current_app
from flask_script import Manager
from application.main import app

log = logging.getLogger(__name__)
manager = Manager(app)


@manager.command
def collect():
    from application.main import insert_sample
    log.info("Collecting data")
    ds = current_app.config['DATA_SOURCES']

    # Insert sample for the serie
    for d in ds:
        r = requests.get(d)
        print(r.json())
        response_dict = r.json()
        for k, v in response_dict.items():
            insert_sample(k, v)


@manager.command
def db_init():
    from application.main import create_tables
    # TODO: Expose safety option
    create_tables()

if __name__ == "__main__":
    manager.run()
