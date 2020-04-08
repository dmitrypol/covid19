import pytest
from app import models, formatters


def test_location_last_confirmed():
    for obj in models.Location.all():
        obj.delete()
    obj1 = models.Location.create(name='KingWashingtonUS')
    obj1.confirmed.update({'03-22-2020':3})
    obj1.save()
    obj2 = models.Location.create(name='WhatcomWashingtonUS')
    obj2.confirmed.update({'03-22-2020':2})
    obj2.save()
    assert formatters.last_confirmed([obj1]) == '3'
    assert formatters.last_confirmed([obj2]) == '2'
    assert formatters.last_confirmed([obj1, obj2]) == '5'


def test_location_last_deaths():
    for obj in models.Location.all():
        obj.delete()
    obj1 = models.Location.create(name='KingWashingtonUS')
    obj1.deaths.update({'03-22-2020':2})
    obj1.save()
    obj2 = models.Location.create(name='WhatcomWashingtonUS')
    obj2.deaths.update({'03-22-2020':1})
    obj2.save()
    assert formatters.last_deaths([obj1]) == '2'
    assert formatters.last_deaths([obj2]) == '1'
    assert formatters.last_deaths([obj1, obj2]) == '3'


def test_location_format_chart_data():
    for obj in models.Location.all():
        obj.delete()
    obj1 = models.Location.create(name='KingWashingtonUS')
    obj1.confirmed.update({'03-22-2020':10, '03-23-2020':15, '03-24-2020':20})
    obj1.deaths.update({'03-22-2020':5, '03-23-2020':6, '03-24-2020':8})
    obj1.save()
    obj2 = models.Location.create(name='WhatcomWashingtonUS')
    obj2.confirmed.update({'03-22-2020':5, '03-23-2020':6, '03-24-2020':7})
    obj2.deaths.update({'03-22-2020':2, '03-23-2020':3, '03-24-2020':3})
    obj2.save()
    assert formatters.format_chart_data([obj1]) == {
        'confirmed': [['03-22-2020', 10.0], ['03-23-2020', 5], ['03-24-2020', 5]],
        'deaths': [['03-22-2020', 5.0], ['03-23-2020', 1], ['03-24-2020', 2]]
        }
    assert formatters.format_chart_data([obj2]) == {
        'confirmed': [['03-22-2020', 5.0], ['03-23-2020', 1], ['03-24-2020', 1]],
        'deaths': [['03-22-2020', 2.0], ['03-23-2020', 1], ['03-24-2020', 0]]
        }
    assert formatters.format_chart_data([obj1, obj2]) == {
        'confirmed': [['03-22-2020', 15], ['03-23-2020', 6], ['03-24-2020', 6]],
        'deaths': [['03-22-2020', 7.0], ['03-23-2020', 2], ['03-24-2020', 2]]
        }


def test_location_row_date_diff():
    row = [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    test = formatters._row_date_diff(row)
    assert test == [['03-22-2020', '100'], ['03-23-2020', 10], ['03-24-2020', 20], ['03-25-2020', 30], ['03-26-2020', 40]]
