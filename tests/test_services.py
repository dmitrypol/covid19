import pytest
from app import APP, services


def test_get_data_index():
    test = services.get_data_index()
    assert test is not None


def _test_get_data_show():
    test = services.get_data_show('valid_key_here')
    assert test == {}


def test_get_data_show_invalid_key():
    test = services.get_data_show('invalid_key')
    assert test == {}


def test_get_import_dates_list():
    test = services.get_import_dates_list()
    assert test[0] == APP.config.get('START_DATE')
