import pytest
from app import scheduler


def test_import_data():
    test = scheduler.schedule_jobs()
    assert test is None
