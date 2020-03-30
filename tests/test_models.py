import pytest
from app import models


def test_search_form():
    assert models.Location() is not None
