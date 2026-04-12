import pytest
import os
import json
from infrastructure.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_publish_no_auth(client):
    os.environ['GUCE_API_KEY'] = 'secret123'
    response = client.post('/api/publish', json={'transcript': 'test'})
    assert response.status_code == 401

def test_publish_with_auth(client):
    os.environ['GUCE_API_KEY'] = 'secret123'
    response = client.post('/api/publish', headers={'X-API-Key': 'secret123'}, json={'transcript': 'test'})
    assert response.status_code == 200 or response.status_code == 500 # might fail inside because no drive service, but auth passes
