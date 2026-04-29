import pytest
from fastapi.testclient import TestClient
import os
import sys

# Add the root directory to PYTHONPATH so main can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_missing_auth_header():
    """Missing auth header should return 403 Forbidden because of HTTPBearer."""
    response = client.post("/api/v1/capture/stream?user_id=user1")
    assert response.status_code in (401, 403)
    assert response.json() == {"detail": "Not authenticated"}

def test_missing_env_variable(monkeypatch):
    """Missing GUCE_API_KEY env variable should return 500 Internal Server Error."""
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post("/api/v1/capture/stream?user_id=user1", headers={"Authorization": "Bearer some-token"})
    assert response.status_code == 500
    assert "GUCE_API_KEY environment variable is not configured" in response.json()["detail"]

def test_invalid_credentials(monkeypatch):
    """Invalid token should return 401 Unauthorized."""
    monkeypatch.setenv("GUCE_API_KEY", "valid-secret-key")
    response = client.post("/api/v1/capture/stream?user_id=user1", headers={"Authorization": "Bearer invalid-token"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}

def test_valid_credentials(monkeypatch):
    """Valid token should return 200 OK and ProjectManifest."""
    monkeypatch.setenv("GUCE_API_KEY", "valid-secret-key")
    response = client.post("/api/v1/capture/stream?user_id=user1", headers={"Authorization": "Bearer valid-secret-key"})
    assert response.status_code == 200
    data = response.json()
    assert "project_id" in data
    assert data["user_id"] == "user1"
    assert data["status"] == "STREAMING"
