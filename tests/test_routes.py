import os, base64
import pytest
from flask import url_for
from app import APP, models


def test_404(client):
    response = client.get('/invalid/url')
    assert response.status_code == 302


def test_index(client):
    response = client.get(url_for('index'))
    assert response.status_code == 200


def test_index_json(client):
    response = client.get(url_for('index', format='json'))
    assert response.status_code == 200


def test_show(client):
    models.Location.create(name='KingWashingtonUS', state='Washington')
    response = client.get(url_for('show', name='KingWashingtonUS'))
    assert response.status_code == 200


def test_show_json(client):
    models.Location.create(name='KingWashingtonUS')
    response = client.get(url_for('show', name='KingWashingtonUS', format='json'))
    assert response.status_code == 200
    #assert 'Washington' in response.json


def test_show_state(client):
    models.Location.create(name='KingWashingtonUS')
    response = client.get(url_for('show', name='Washington'))
    assert response.status_code == 200


def test_show_state_json(client):
    models.Location.create(name='KingWashingtonUS')
    response = client.get(url_for('show', name='Washington', format='json'))
    assert response.status_code == 200


def _test_show_object_not_found(client):
    response = client.get(url_for('show', name='invalid'))
    assert response.status_code == 302


def test_rq(client):
    response = client.get(url_for('rq_dashboard.overview'))
    assert response.status_code == 401


def _test_rq_auth(client):
    auth = f"{os.environ.get('RQ_DASHBOARD_USERNAME')}:{os.environ.get('RQ_DASHBOARD_PASSWORD')}"
    headers = {'Authorization': 'Basic ' + base64.b64encode(auth)}
    response = client.get(url_for('rq_dashboard.overview'), headers=headers)
    assert response.status_code == 200
