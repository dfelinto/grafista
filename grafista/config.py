import os.path


class Config(object):
    DEBUG = True
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    DATABASE = 'grafista.sqlite'
    DATA_SOURCES = [
        {'url': 'https://store.blender.org/product-counter/?prod=cloud',
         'series': [
             {'name': 'total_sold',
              'description': 'Subscriptions',
              'sample_unit': 'People'}
         ]},
    ]

