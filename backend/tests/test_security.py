import pytest
import os
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_capture_stream_missing_auth_header(client):
    response = client.post("/api/v1/capture/stream?user_id=test_user")
    # Missing authorization header may return 401 or 403 depending on FastAPI version
    assert response.status_code in [401, 403]
    assert response.json() == {"detail": "Not authenticated"}

def test_capture_stream_invalid_token(client, monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "secret_key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Key"}

def test_capture_stream_missing_env_var(client, monkeypatch):
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer some_token"}
    )
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error: Authentication configuration missing."}

def test_capture_stream_valid_token(client, monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "valid_secret_key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer valid_secret_key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "test_user"
    assert data["status"] == "STREAMING"
