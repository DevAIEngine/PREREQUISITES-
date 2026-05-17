import pytest
from fastapi.testclient import TestClient
import os

from backend.main import app

client = TestClient(app)

def test_capture_stream_no_auth():
    response = client.post("/api/v1/capture/stream", params={"user_id": "test_user"})
    # Depending on FastAPI version, it might be 401 or 403 for missing header
    assert response.status_code in [401, 403]

def test_capture_stream_invalid_auth(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "real_key")
    headers = {"Authorization": "Bearer invalid_key"}
    response = client.post("/api/v1/capture/stream", params={"user_id": "test_user"}, headers=headers)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API Key"

def test_capture_stream_valid_auth(monkeypatch):
    test_key = "secure_test_api_key_123"
    monkeypatch.setenv("GUCE_API_KEY", test_key)

    headers = {"Authorization": f"Bearer {test_key}"}
    response = client.post("/api/v1/capture/stream", params={"user_id": "test_user"}, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "test_user"
    assert data["status"] == "STREAMING"
    assert "project_id" in data
