import pytest
from app import APP, services


def test_get_data():
    test = services.get_data()
    assert test is not None


def test_get_import_dates_list():
    test = services.get_import_dates_list()
    assert test[0] == APP.config.get('START_DATE')
