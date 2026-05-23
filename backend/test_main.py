import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_start_capture_stream_missing_auth_header():
    # Attempting to access without an Authorization header
    response = client.post("/api/v1/capture/stream?user_id=test_user")
    assert response.status_code in [401, 403]

def test_start_capture_stream_missing_env_var(monkeypatch):
    # Ensure GUCE_API_KEY is not set
    monkeypatch.delenv("GUCE_API_KEY", raising=False)

    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer dummy_token"}
    )
    assert response.status_code == 500
    assert response.json()["detail"] == "Internal Server Configuration Error"

def test_start_capture_stream_invalid_api_key(monkeypatch):
    # Set the environment variable
    monkeypatch.setenv("GUCE_API_KEY", "secret_key_123")

    # Use wrong token
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer wrong_token"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API Key"

def test_start_capture_stream_valid_api_key(monkeypatch):
    # Set the environment variable
    monkeypatch.setenv("GUCE_API_KEY", "secret_key_123")

    # Use correct token
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer secret_key_123"}
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == "test_user"
    assert response.json()["status"] == "STREAMING"
