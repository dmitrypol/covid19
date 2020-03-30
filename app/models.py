''' varous models '''
from walrus import Model, TextField, HashField
from . import WALRUS_DB


class Location(Model):
    __database__ = WALRUS_DB
    # __namespace__ = 'my-app'
    name = TextField(primary_key=True)
    county = TextField(index=False)
    state = TextField(index=False)
    country = TextField(index=False)
    confirmed = HashField()
    deaths = HashField()
    recovered = HashField()
    active = HashField()
