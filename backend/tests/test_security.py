import pytest
import os
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_stream_endpoint_missing_token():
    """Test that a missing authorization header returns 403 Forbidden."""
    response = client.post("/api/v1/capture/stream", params={"user_id": "test_user"})
    assert response.status_code in [401, 403]
    assert response.json()["detail"] == "Not authenticated"

def test_stream_endpoint_invalid_token(monkeypatch):
    """Test that an invalid token returns 401 Unauthorized."""
    monkeypatch.setenv("GUCE_API_KEY", "correct_secret_key")
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer wrong_secret_key"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication credentials"

def test_stream_endpoint_missing_env_var(monkeypatch):
    """Test that missing GUCE_API_KEY env var fails securely with 500."""
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer any_key"}
    )
    assert response.status_code == 500
    assert response.json()["detail"] == "Server configuration error"

def test_stream_endpoint_valid_token(monkeypatch):
    """Test that a valid token returns 200 OK."""
    monkeypatch.setenv("GUCE_API_KEY", "correct_secret_key")
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer correct_secret_key"}
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == "test_user"
    assert response.json()["status"] == "STREAMING"
