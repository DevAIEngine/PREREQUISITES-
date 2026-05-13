import pytest
import os
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_capture_stream_missing_auth():
    response = client.post("/api/v1/capture/stream?user_id=user123")
    assert response.status_code in [401, 403]
    assert response.json() == {"detail": "Not authenticated"}

def test_capture_stream_invalid_token(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "secret123")
    response = client.post("/api/v1/capture/stream?user_id=user123", headers={"Authorization": "Bearer badtoken"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid or missing API Key"}

def test_capture_stream_valid_token(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "secret123")
    response = client.post("/api/v1/capture/stream?user_id=user123", headers={"Authorization": "Bearer secret123"})
    assert response.status_code == 200
    assert response.json()["status"] == "STREAMING"
