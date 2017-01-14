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
    for source in current_app.config['DATA_SOURCES']:
        print('Collecting data from {}'.format(source['url']))
        # Insert sample for the series
        r = requests.get(source['url'])
        response_dict = r.json()
        for d, v in response_dict.items():
            if d in [s['name'] for s in source['series']]:
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
def init_db():
    from application.main import init_db
    # TODO: Expose safety option
    init_db()


@manager.command
def init_series():
    """Create series from DATA_SOURCES"""
    from application.models import Series
    for data_source in current_app.config['DATA_SOURCES']:
        for serie in data_source['series']:
            s, created = Series.get_or_create(name=serie['name'])
            if created:
                print('Created {}'.format(s))

if __name__ == "__main__":
    manager.run()
