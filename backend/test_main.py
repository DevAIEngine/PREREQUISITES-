import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_start_capture_stream_missing_token():
    response = client.post("/api/v1/capture/stream?user_id=123")
    assert response.status_code in [401, 403]

def test_start_capture_stream_invalid_token(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "secret-key")
    response = client.post(
        "/api/v1/capture/stream?user_id=123",
        headers={"Authorization": "Bearer wrong-key"}
    )
    assert response.status_code == 401

def test_start_capture_stream_missing_env_var(monkeypatch):
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream?user_id=123",
        headers={"Authorization": "Bearer any-key"}
    )
    assert response.status_code == 500

def test_start_capture_stream_success(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "secret-key")
    response = client.post(
        "/api/v1/capture/stream?user_id=123",
        headers={"Authorization": "Bearer secret-key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "STREAMING"
    assert data["user_id"] == "123"
