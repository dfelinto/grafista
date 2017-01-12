import logging
import requests
from flask import current_app
from flask_script import Manager
from application.main import app

log = logging.getLogger(__name__)
manager = Manager(app)


@manager.command
def collect():
    """Populates the database from the data source
    """
    from application.main import insert_sample
    ds = current_app.config['DATA_SOURCES']
    print('Collecting data from {}'.format(ds))
    # Insert sample for the series
    for source in ds:
        r = requests.get(source)
        response_dict = r.json()
        for d, v in response_dict.items():
            print('Storing {} {}'.format(d, v))
            insert_sample(d, v)


@manager.command
def insert_sample(serie_url, value, timestamp=None):
    """Manually inserts a sample to the database
    """
    from application.main import insert_sample
    insert_sample(serie_url, value, timestamp)


@manager.command
def insert_samples(csv_file):
    """Populates the database with a .csv file
    """
    from application.main import insert_sample
    import csv
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert_sample(
                    row['serie_url'],
                    row['value'],
                    row['timestamp'])


@manager.command
def db_init():
    from application.main import init_db
    # TODO: Expose safety option
    init_db()

if __name__ == "__main__":
    manager.run()
