import pytest
from infrastructure.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_scenes_no_json(client):
    rv = client.post('/veo-studio/generate-scenes', data="not json")
    assert rv.status_code == 400 or rv.status_code == 415

def test_generate_scenes_invalid_scenes(client):
    rv = client.post('/veo-studio/generate-scenes', json={"scenes": "not_a_list"})
    assert rv.status_code == 400

def test_generate_scenes_invalid_duration(client):
    rv = client.post('/veo-studio/generate-scenes', json={"scenes": [{"duration": "str"}]})
    assert rv.status_code == 400

def test_generate_scenes_valid(client):
    rv = client.post('/veo-studio/generate-scenes', json={"scenes": [{"duration": 10}, {"duration": 20.5}]})
    assert rv.status_code == 200
    assert rv.json['totalDuration'] == 30.5
