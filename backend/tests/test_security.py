import os
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

@pytest.fixture
def valid_token_env(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "super-secret-key")

@pytest.fixture
def missing_token_env(monkeypatch):
    monkeypatch.delenv("GUCE_API_KEY", raising=False)

def test_start_capture_stream_valid_token(valid_token_env):
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer super-secret-key"})
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "123"
    assert data["status"] == "STREAMING"
    assert "project_id" in data

def test_start_capture_stream_invalid_token(valid_token_env):
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer wrong-key"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Key"}

def test_start_capture_stream_missing_token_env(missing_token_env):
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer any-key"})
    assert response.status_code == 500
    assert response.json() == {"detail": "Server misconfiguration: GUCE_API_KEY missing"}

def test_start_capture_stream_missing_auth_header():
    # Will fail early inside HTTPBearer because the header is missing
    response = client.post("/api/v1/capture/stream?user_id=123")
    assert response.status_code == 403 or response.status_code == 401 # HTTPBearer returns 403 on missing auth header by default
    assert response.json() == {"detail": "Not authenticated"}
