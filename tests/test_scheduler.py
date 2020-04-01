import pytest
from app import scheduler


def test_import_data():
    test = scheduler.import_data()
    assert test is None


def test_refresh_hp():
    test = scheduler.refresh_hp()
    assert test is None
