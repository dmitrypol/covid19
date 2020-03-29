import pytest
from flask import url_for
from app import APP


def test_index(client):
    response = client.get(url_for('index'))
    assert response.status_code == 200


def test_index_json(client):
    response = client.get(url_for('index', format='json'))
    assert response.status_code == 200
