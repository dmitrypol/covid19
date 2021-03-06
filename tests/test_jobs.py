import pytest
import vcr
from app import APP, jobs


def test_get_url():
    test = jobs.get_url('http://localhost:5000')
    assert test is None


@vcr.use_cassette('tests/fixtures/vcr_cassettes/import_data.yml')
def test_import_data():
    test = jobs.import_data(date=APP.config.get('START_DATE'))
    assert test is None


def _test_process_row():
    pass


def test_format_date():
    test = jobs._format_date('2020-03-28 23:05:37')
    assert test == '03-28-2020'
    test = jobs._format_date('3/23/20 23:45')
    assert test == '03-23-2020'
