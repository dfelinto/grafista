import datetime
from peewee import Model, CharField, DateTimeField, ForeignKeyField
from . import db


class BaseModel(Model):
    class Meta:
        database = db


class Series(BaseModel):
    """Table storing the definition of the samples, for example the user count
    or the daily income. A serie is composed of samples, which refer to it.
    """
    name = CharField(unique=True)  # users_total_count
    description = CharField(null=True)
    sample_unit = CharField(null=True)  # People, EUR

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
