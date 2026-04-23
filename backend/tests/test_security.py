import pytest
from fastapi.testclient import TestClient
import os
import sys

# Add the backend directory to sys.path to allow importing main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

client = TestClient(app)

# Test API Key for unit testing
TEST_API_KEY = "test_guce_api_key_2024"

@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    """Set the GUCE_API_KEY environment variable for tests."""
    monkeypatch.setenv("GUCE_API_KEY", TEST_API_KEY)

def test_start_capture_stream_no_auth():
    """Verify that the endpoint returns 403 when no authorization header is provided."""
    response = client.post("/api/v1/capture/stream")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}

def test_start_capture_stream_invalid_auth():
    """Verify that the endpoint returns 401 when an invalid API key is provided."""
    response = client.post(
        "/api/v1/capture/stream",
        headers={"Authorization": "Bearer invalid_key"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid or missing API Key"}

def test_start_capture_stream_valid_auth():
    """Verify that the endpoint returns 200 when a valid API key is provided."""
    response = client.post(
        "/api/v1/capture/stream",
        headers={"Authorization": f"Bearer {TEST_API_KEY}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "authenticated_user"
    assert data["status"] == "STREAMING"
    assert "guce_proj_" in data["project_id"]

def test_start_capture_stream_misconfigured_server(monkeypatch):
    """Verify that the endpoint returns 500 when the API key is not set on the server."""
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream",
        headers={"Authorization": f"Bearer {TEST_API_KEY}"}
    )
    assert response.status_code == 500
    assert response.json() == {"detail": "Server configuration error"}

def test_health_check_remains_public():
    """Verify that the health check endpoint remains accessible without authentication."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "4.0.0"}
