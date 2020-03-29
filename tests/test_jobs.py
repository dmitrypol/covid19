import pytest
import vcr
from app import jobs


@vcr.use_cassette('tests/fixtures/vcr_cassettes/import_data.yml')
def test_import_data():
    test = jobs.import_data()
    assert test is None


def _test_process_row():
    pass


def _test_format_date():
    pass