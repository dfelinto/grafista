import logging
from flask import jsonify
from .models import Samples, Series
from . import app, db

log = logging.getLogger(__name__)


def create_tables(safe=True):
    # Create table for each model if it does not exist.
    db.create_tables([Series, Samples], safe=safe)


@app.route('/series')
def index():
    series = []
    for s in Series.select():
        series.append(s.name)
    return jsonify(series=series)


@app.route('/series/<name>')
def serie_view(name):
    serie = Series.get(name=name)
    samples = []
    for s in Samples.select().where(Samples.serie == serie.id):
        samples.append((s.value, s.timestamp))
    return jsonify(samples=samples)


def insert_sample(serie_name, value):
    # Check if serie exists
    if isinstance(value, int):
        value_type = 'int'
    elif isinstance(value, float):
        value_type = 'float'
    else:
        value_type = 'str'

    serie, created = Series.create_or_get(name=serie_name)
    sample = Samples(serie=serie.id, value=str(value), value_type=value_type)
    log.debug('Inserting {}'.format(sample))
    sample.save()
