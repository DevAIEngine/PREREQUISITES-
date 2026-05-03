import pytest
from fastapi.testclient import TestClient
import os
import hmac
from backend.main import app

client = TestClient(app)

def test_capture_stream_no_auth():
    # Attempt to access the endpoint without authorization header
    response = client.post("/api/v1/capture/stream?user_id=test_user")
    # Missing auth header defaults to 403 Forbidden in modern FastAPI versions, sometimes 401.
    assert response.status_code in [401, 403]
    assert "Not authenticated" in response.json()["detail"] or "Not authenticated" == response.json()["detail"]

def test_capture_stream_invalid_auth(monkeypatch):
    # Set a fake valid token
    monkeypatch.setenv("GUCE_API_KEY", "super_secret_key")

    # Attempt to access the endpoint with an invalid token
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authentication credentials"

def test_capture_stream_valid_auth(monkeypatch):
    # Set a fake valid token
    monkeypatch.setenv("GUCE_API_KEY", "super_secret_key")

    # Attempt to access the endpoint with a valid token
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer super_secret_key"}
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == "test_user"

def test_capture_stream_missing_env_var(monkeypatch):
    # Ensure GUCE_API_KEY is not set
    monkeypatch.delenv("GUCE_API_KEY", raising=False)

    # Attempt to access the endpoint
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer super_secret_key"}
    )
    assert response.status_code == 500
    assert response.json()["detail"] == "Server configuration error: GUCE_API_KEY not set"
