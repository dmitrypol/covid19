''' varous schemas '''
# pylint: disable = no-self-use, too-few-public-methods
from flask_marshmallow.fields import fields
from . import MA


class Location(MA.Schema):
    class Meta:
        fields = ('name', 'county', 'state', 'country', 'last_confirmed', 'last_deaths', 'chart_data')
        ordered = True

    name = fields.Str()
    county = fields.Str()
    state = fields.Str()
    country = fields.Str()
    chart_data = fields.Method('obj_chart_data')
    last_confirmed = fields.Method('obj_last_confirmed')
    last_deaths = fields.Method('obj_last_deaths')


    def obj_chart_data(self, obj):
        return obj.format_chart_data()


    def obj_last_confirmed(self, obj):
        return obj.last_confirmed()


    def obj_last_deaths(self, obj):
        return obj.last_deaths()


    # def obj_confirmed(self, obj):
    #     return obj.confirmed.items()
