import datetime
from peewee import Model, CharField, DateTimeField, ForeignKeyField
from flask import current_app
from . import db


class BaseModel(Model):
    class Meta:
        database = db


class Series(BaseModel):
    """Table storing the definition of the samples, for example the user count
    or the daily income. A serie is composed of samples, which refer to it.
    """
    name = CharField(unique=True)  # users_total_count
    description = CharField(null=True)  # Subscribers
    sample_unit = CharField(null=True)  # People, EUR

    @staticmethod
    def _get_from_data_sources(name):
        for source in current_app.config['DATA_SOURCES']:
            series = next((item for item in source['series']
                           if item['name'] == name), None)
            if series:
                return series

    @classmethod
    def get_or_create(cls, name):
        """We override the original so that we need to pass only the name. With
        the name, we can find the series properties in the config.py.
        """

        series = cls._get_from_data_sources(name)

        if series is None:
            raise AttributeError(
                'Name {} was not found in DATA_SOURCES'.format(name))

        inst, created = cls.create_or_get(name=name)
        if created:
            if 'description' in series:
                inst.description = series['description']
            if 'sample_unit' in series:
                inst.sample_unit = series['sample_unit']
            inst.save()
        return inst, created

    def __unicode__(self):
        return self.name


class Samples(BaseModel):
    serie = ForeignKeyField(Series, related_name='samples', null=False)
    timestamp = DateTimeField(default=datetime.datetime.now)
    value = CharField()
    value_type = CharField(choices=[
        ('int', 'Integer'),
        ('str', 'String'),
        ('float', 'Float')])

    def __unicode__(self):
        return self.value
