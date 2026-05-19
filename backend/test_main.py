import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_capture_stream_no_auth():
    # Attempting to access without auth header
    response = client.post("/api/v1/capture/stream", params={"user_id": "test_user"})
    # FastAPI returns 403 for missing HTTPBearer dependency
    assert response.status_code in [401, 403]

def test_capture_stream_missing_env_var(monkeypatch):
    # Ensure env var is not set
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer any_key"}
    )
    # Should raise 500 when environment variable is missing
    assert response.status_code == 500

def test_capture_stream_invalid_key(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_secret_key")
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer wrong_key"}
    )
    assert response.status_code == 401

def test_capture_stream_valid_key(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_secret_key")
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer correct_secret_key"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "STREAMING"
