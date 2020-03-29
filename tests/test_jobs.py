import pytest
from app import jobs


def test_import_data():
    test = jobs.import_data()
    assert test is None
