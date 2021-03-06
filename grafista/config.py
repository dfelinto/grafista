import os.path

TITLE = 'Grafista'
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'grafista.sqlite'
DATA_SOURCES = []  # See README.md for an example
APPLICATION_ROOT = ''  # Modify if we run on a subdomain, line /stats

# See https://docs.python.org/2/library/logging.config.html#configuration-dictionary-schema
LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)-15s %(levelname)8s %(name)s %(message)s'}
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stderr',
        }
    },
    'loggers': {
        'application': {'level': 'INFO'},
        'werkzeug': {'level': 'INFO'},
    },
    'root': {
        'level': 'WARNING',
        'handlers': [
            'console',
        ],
    }
}
