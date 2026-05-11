import pytest
from fastapi.testclient import TestClient
from backend.main import app
import os

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

def test_start_capture_stream_no_auth():
    response = client.post("/api/v1/capture/stream?user_id=123")
    assert response.status_code in [401, 403]

def test_start_capture_stream_invalid_auth():
    os.environ["GUCE_API_KEY"] = "secret"
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer wrong"})
    assert response.status_code == 401

def test_start_capture_stream_valid_auth():
    os.environ["GUCE_API_KEY"] = "secret"
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer secret"})
    assert response.status_code == 200
