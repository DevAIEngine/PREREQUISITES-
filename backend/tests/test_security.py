import os
import pytest
from fastapi.testclient import TestClient
from backend.main import app

# Fixtures for test app and environment
@pytest.fixture
def client():
    return TestClient(app)

def test_missing_api_key_env_var(client, monkeypatch):
    """Test that the server returns a 500 when GUCE_API_KEY is not configured."""
    monkeypatch.delenv("GUCE_API_KEY", raising=False)

    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer some_token"}
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Server configuration error"


def test_missing_authorization_header(client, monkeypatch):
    """Test that a missing Authorization header returns a 403 status code."""
    monkeypatch.setenv("GUCE_API_KEY", "test_secret_key")

    # Missing Auth header defaults to 403 from FastAPI's HTTPBearer
    response = client.post("/api/v1/capture/stream?user_id=test_user")
    assert response.status_code in [401, 403]


def test_invalid_api_key(client, monkeypatch):
    """Test that providing an invalid token returns a 401 status code."""
    monkeypatch.setenv("GUCE_API_KEY", "test_secret_key")

    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API Key"


def test_valid_api_key(client, monkeypatch):
    """Test that providing a valid token returns a 200 OK and a valid manifest."""
    monkeypatch.setenv("GUCE_API_KEY", "test_secret_key")

    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer test_secret_key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "test_user"
    assert data["status"] == "STREAMING"
    assert "project_id" in data
