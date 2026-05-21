import pytest
from fastapi.testclient import TestClient
from backend.main import app
import os

client = TestClient(app)

def test_start_capture_stream_no_auth():
    # Sending request without Authorization header
    response = client.post("/api/v1/capture/stream?user_id=123")
    assert response.status_code in [401, 403]

def test_start_capture_stream_missing_env_var(monkeypatch):
    # Ensure GUCE_API_KEY is not set
    monkeypatch.delenv("GUCE_API_KEY", raising=False)

    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer dummy_token"})
    assert response.status_code == 500
    assert "Missing GUCE_API_KEY environment variable" in response.json()["detail"]

def test_start_capture_stream_invalid_key(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_secret_key")

    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer wrong_token"})
    assert response.status_code == 401
    assert "Invalid API Key" in response.json()["detail"]

def test_start_capture_stream_valid_key(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_secret_key")

    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer correct_secret_key"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "STREAMING"
    assert data["user_id"] == "123"
    assert "guce_proj_" in data["project_id"]
