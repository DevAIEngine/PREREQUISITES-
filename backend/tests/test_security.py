import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_capture_stream_no_auth():
    # Should return 403 Forbidden due to missing HTTPBearer header
    response = client.post("/api/v1/capture/stream?user_id=test_user")
    assert response.status_code in [401, 403]
    assert response.json() == {"detail": "Not authenticated"}

def test_capture_stream_invalid_auth(monkeypatch):
    # Should return 401 Unauthorized due to invalid credentials
    monkeypatch.setenv("GUCE_API_KEY", "correct-secret-key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer wrong-secret-key"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Key"}

def test_capture_stream_missing_env_var(monkeypatch):
    # Should return 500 Internal Server Error due to missing GUCE_API_KEY
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer some-secret-key"}
    )
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Configuration Error"}

def test_capture_stream_valid_auth(monkeypatch):
    # Should succeed with valid credentials
    monkeypatch.setenv("GUCE_API_KEY", "correct-secret-key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer correct-secret-key"}
    )
    assert response.status_code == 200
    assert "project_id" in response.json()
