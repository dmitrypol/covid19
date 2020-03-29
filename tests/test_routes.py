import os, base64
import pytest
from flask import url_for
from app import APP


def test_index(client):
    response = client.get(url_for('index'))
    assert response.status_code == 200


def test_index_json(client):
    response = client.get(url_for('index', format='json'))
    assert response.status_code == 200


def test_rq(client):
    response = client.get(url_for('rq_dashboard.overview'))
    assert response.status_code == 401


def _test_rq_auth(client):
    auth = f"{os.environ.get('RQ_DASHBOARD_USERNAME')}:{os.environ.get('RQ_DASHBOARD_PASSWORD')}"
    headers = {'Authorization': 'Basic ' + base64.b64encode(auth)}
    response = client.get(url_for('rq_dashboard.overview'), headers=headers)
    assert response.status_code == 200
