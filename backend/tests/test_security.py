import pytest
from fastapi.testclient import TestClient
import os
import sys

# Required to mock dependencies before importing the app
with pytest.MonkeyPatch.context() as m:
    pass

from backend.main import app

client = TestClient(app)

def test_start_capture_stream_valid_token(monkeypatch):
    """Test that a valid token allows access to the stream endpoint."""
    valid_token = "super_secret_token_123"
    monkeypatch.setenv("GUCE_API_KEY", valid_token)

    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": f"Bearer {valid_token}"}
    )

    assert response.status_code == 200
    assert response.json()["user_id"] == "test_user"
    assert response.json()["status"] == "STREAMING"

def test_start_capture_stream_invalid_token(monkeypatch):
    """Test that an invalid token returns 401 Unauthorized."""
    valid_token = "super_secret_token_123"
    monkeypatch.setenv("GUCE_API_KEY", valid_token)

    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer wrong_token"}
    )

    assert response.status_code == 401
    assert "Invalid API Key" in response.json()["detail"]

def test_start_capture_stream_missing_token(monkeypatch):
    """Test that a missing Authorization header returns 403 Forbidden (from HTTPBearer)."""
    valid_token = "super_secret_token_123"
    monkeypatch.setenv("GUCE_API_KEY", valid_token)

    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"}
    )

    # fastapi HTTPBearer returns 403 if it is missing
    assert response.status_code in [401, 403]

def test_start_capture_stream_missing_env_var(monkeypatch):
    """Test that if GUCE_API_KEY is not set, the endpoint fails securely with 500."""
    # Ensure GUCE_API_KEY is not in the environment
    monkeypatch.delenv("GUCE_API_KEY", raising=False)

    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer some_token"}
    )

    assert response.status_code == 500
    assert "Internal Server Error" in response.json()["detail"]
