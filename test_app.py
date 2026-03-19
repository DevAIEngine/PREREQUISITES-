import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_process_request_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Aurora OSIRIS Core Engine" in response.data

def test_process_request_post(client):
    response = client.post('/')
    assert response.status_code == 200
    assert response.json == {"optimization": "complete", "stream": "tensorized"}

def test_phantom_status(client):
    response = client.get('/phantom/status')
    assert response.status_code == 200
    assert response.json == {"status": "phantom active"}
