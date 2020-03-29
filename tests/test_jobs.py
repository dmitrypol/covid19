import pytest
import vcr
from app import jobs


#@vcr.use_cassette('tests/fixtures/vcr_cassettes/import_data.yml')
def test_import_data():
    test = jobs.import_data()
    assert test is None


def _test_process_row():
    pass


def _test_format_date():
    test = jobs._format_date('2020-03-28 23:05:37')
    assert test == '03-28-2020'
    test = jobs._format_date('3/22/20 23:45')
    assert test == '03-22-2020'
