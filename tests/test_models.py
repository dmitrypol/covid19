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
