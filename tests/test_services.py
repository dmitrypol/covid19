import pytest
from freezegun import freeze_time
from app import APP, services


def test_get_import_dates_list():
    freezer = freeze_time('2020-03-24 12:00:00')
    freezer.start()
    test = services.get_import_dates_list()
    assert test == [APP.config.get('START_DATE'), '03-23-2020', '03-24-2020']
    freezer.stop()


def _test_format_chart_data():
    pass


def test_row_date_diff():
    row = [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    test = services.row_date_diff(row)
    assert test == [['03-22-2020', '100'], ['03-23-2020', '10'], ['03-24-2020', '20'], ['03-25-2020', '30'], ['03-26-2020', '40']]
