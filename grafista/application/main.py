import logging
from flask import abort, jsonify, render_template, request
import datetime
from .models import Samples, Series
from . import app, db

log = logging.getLogger(__name__)


def init_db(safe=True):
    # Create table for each model if it does not exist.
    db.create_tables([Series, Samples], safe=safe)


def insert_sample(serie_name, value, timestamp=None):
    # Check if series exists
    if isinstance(value, float):
        value_type = 'str'
    else:
        value_type = 'int'

    serie, created = Series.get_or_create(serie_name)
    sample = Samples(serie=serie.id, value=str(value), value_type=value_type)

    if timestamp:
        try:
            sample.timestamp = datetime.datetime.strptime(timestamp, '%Y-%m-%d')
        except ValueError:
            log.debug('Invalid timestamp format {}, should be {}').format(
                timestamp, '%Y-%m-%d'
            )

    log.debug('Inserting {}'.format(sample))
    sample.save()


def get_or_404(item_class, **query):
    try:
        item = item_class.get(**query)
    except item_class.DoesNotExist:
        return abort(404)
    return item


@app.route('/series/')
def series_index():
    series = []
    for s in Series.select():
        series.append(s.name)
    return jsonify(series=series)


@app.route('/series/<name>')
def series_view(name):
    # Check if series exists
    serie = get_or_404(Series, name=name)
    request_format = request.args.get('format')
    if request_format and request_format == 'json':
        samples_query = Samples.select().where(Samples.serie == serie.id)
        samples = [(s.timestamp, int(s.value)) for s in samples_query]
        return jsonify(samples=samples)
    else:
        return render_template('series_view.pug', serie=serie)


@app.route('/')
def dashboard():
    return render_template('dashboard.pug')
