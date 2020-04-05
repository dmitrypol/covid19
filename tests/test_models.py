import pytest
from app import models


def test_location():
    assert models.Location() is not None
