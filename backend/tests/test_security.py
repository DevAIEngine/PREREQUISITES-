import os
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_missing_api_key_env_var(monkeypatch):
    """Test that missing GUCE_API_KEY env var returns 500 error to prevent insecure default states."""
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer any_token"})
    assert response.status_code == 500
    assert response.json()["detail"] == "Internal Server Error: Missing Configuration"

def test_missing_authorization_header(monkeypatch):
    """Test that missing Authorization header returns 401 or 403."""
    monkeypatch.setenv("GUCE_API_KEY", "test_secret_key")
    response = client.post("/api/v1/capture/stream?user_id=123")
    assert response.status_code in [401, 403]
    # Depending on fastapi version HTTPBearer responds with either 401 or 403

def test_invalid_token(monkeypatch):
    """Test that an invalid token returns 401."""
    monkeypatch.setenv("GUCE_API_KEY", "test_secret_key")
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API Key"

def test_valid_token(monkeypatch):
    """Test that a valid token returns 200 OK."""
    monkeypatch.setenv("GUCE_API_KEY", "test_secret_key")
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer test_secret_key"})
    assert response.status_code == 200
    assert "project_id" in response.json()
