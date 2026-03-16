import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_engine_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "operational", "version": "1.0.0"}

def test_run_valid_test():
    response = client.get("/engine/test/42")
    assert response.status_code == 200
    assert response.json() == {"message": "Test 42 executed successfully"}

def test_run_invalid_test():
    response = client.get("/engine/test/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid test ID"}

def test_run_invalid_test_negative():
    response = client.get("/engine/test/-5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid test ID"}
