import pytest
from app import schemas, models


def test_location():
    assert schemas.Location() is not None


def test_location_chart_data():
    obj = models.Location.create(name='KingWashingtonUS')
    assert schemas.Location().obj_chart_data(obj) is not None


def test_location_last_confirmed():
    obj = models.Location.create(name='KingWashingtonUS')
    assert schemas.Location().obj_last_confirmed(obj) is not None


def test_location_last_deaths():
    obj = models.Location.create(name='KingWashingtonUS')
    assert schemas.Location().obj_last_deaths(obj) is not None
