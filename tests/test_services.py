import pytest
from freezegun import freeze_time
from app import APP, services


def test_get_import_dates_list():
    freezer = freeze_time('2020-03-24 12:00:00')
    freezer.start()
    test = services.get_import_dates_list()
    assert test == [APP.config.get('START_DATE'), '03-23-2020', '03-24-2020']
    freezer.stop()
