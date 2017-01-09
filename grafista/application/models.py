import datetime
from peewee import CharField, DateTimeField, ForeignKeyField
from . import db


class Series(db.Model):
    """Table storing the definition of the samples, for example the user count
    or the daily income. A serie is composed of samples, which refer to it.
    """
    name = CharField(null=False, unique=True)  # users_total_count
    description = CharField()
    sample_unit = CharField()  # People, EUR

    def __unicode__(self):
        return self.name


class Samples(db.Model):
    serie = ForeignKeyField(Series, related_name='samples', null=False)
    timestamp = DateTimeField(default=datetime.datetime.now)
    value = CharField(null=False)
    value_type = CharField(choices=[
        ('int', 'Integer'),
        ('str', 'String'),
        ('float', 'Float')])

    def __unicode__(self):
        return self.value
