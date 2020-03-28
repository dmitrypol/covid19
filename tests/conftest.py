import pytest
from app import APP


@pytest.fixture
def app():
    return APP
