import os.path


class Config(object):
    DEBUG = True
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    DATABASE = 'grafista.sqlite'
    # TODO: introduce a list of keys to keep from the response
    DATA_SOURCES = {'https://store.blender.org/product-counter/?prod=cloud',}
