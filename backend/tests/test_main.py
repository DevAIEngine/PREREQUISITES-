import pytest
from fastapi.testclient import TestClient
from backend.main import app
import os

client = TestClient(app)

def test_start_capture_stream_no_auth():
    response = client.post("/api/v1/capture/stream?user_id=test_user")
    assert response.status_code in [401, 403]

def test_start_capture_stream_invalid_auth(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer wrong_key"}
    )
    assert response.status_code == 401

def test_start_capture_stream_valid_auth(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_key")
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer correct_key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "test_user"
    assert data["status"] == "STREAMING"
    assert data["project_id"].startswith("guce_proj_")

def test_start_capture_stream_missing_env_var(monkeypatch):
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream?user_id=test_user",
        headers={"Authorization": "Bearer any_key"}
    )
    assert response.status_code == 500
