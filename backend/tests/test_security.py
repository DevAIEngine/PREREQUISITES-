import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_start_capture_stream_unauthorized():
    response = client.post("/api/v1/capture/stream?user_id=test_user")
    assert response.status_code == 403 or response.status_code == 401

def test_start_capture_stream_invalid_token(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "secret_key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid authentication credentials"}

def test_start_capture_stream_server_misconfiguration(monkeypatch):
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer some_token"}
    )
    assert response.status_code == 500
    assert response.json() == {"detail": "Server misconfiguration"}

def test_start_capture_stream_authorized(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "secret_key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer secret_key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "project_id" in data
    assert data["user_id"] == "test_user"
    assert data["status"] == "STREAMING"
