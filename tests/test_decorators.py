import pytest
from app import models, decorators


def test_location_last_confirmed():
    obj = models.Location.create(name='KingWashingtonUS')
    obj.confirmed.update({'03-22-2020':2})
    obj.save()
    assert decorators.last_confirmed(obj) == '2'


def test_location_last_deaths():
    obj = models.Location.create(name='KingWashingtonUS')
    obj.deaths.update({'03-22-2020':1})
    obj.save()
    assert decorators.last_deaths(obj) == '1'


def test_location_format_chart_data():
    obj = models.Location.create(name='KingWashingtonUS')
    obj.confirmed.update({'03-22-2020':2})
    obj.deaths.update({'03-22-2020':1})
    obj.save()
    assert decorators.format_chart_data(obj) == {'confirmed': [['03-22-2020', '2']], 'deaths': [['03-22-2020', '1']]}


def test_location_row_date_diff():
    row = [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    test = decorators._row_date_diff(row)
    assert test == [['03-22-2020', '100'], ['03-23-2020', '10'], ['03-24-2020', '20'], ['03-25-2020', '30'], ['03-26-2020', '40']]
