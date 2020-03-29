import pytest
from app import services


def test_get_data():
    test = services.get_data()
    assert test is not None
