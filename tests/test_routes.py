import pytest
from flask import url_for
from app import APP


def test_root(client):
    response = client.get(url_for('root'))
    assert response.status_code == 200
