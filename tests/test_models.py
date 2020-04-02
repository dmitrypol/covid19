import pytest
from app import models


def test_location():
    assert models.Location() is not None


def test_location_last_confirmed():
    obj = models.Location.create(name='KingWashingtonUS')
    assert obj.last_confirmed() is not None


def test_location_last_deaths():
    obj = models.Location.create(name='KingWashingtonUS')
    assert obj.last_deaths() is not None


def _test_location_format_chart_data():
    pass


def test_location_row_date_diff():
    obj = models.Location.create(name='KingWashingtonUS')
    row = [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    test = obj._row_date_diff(row)
    assert test == [['03-22-2020', '100'], ['03-23-2020', '10'], ['03-24-2020', '20'], ['03-25-2020', '30'], ['03-26-2020', '40']]
