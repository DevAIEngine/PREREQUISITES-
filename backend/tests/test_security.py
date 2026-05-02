import pytest
from fastapi.testclient import TestClient
import os
import sys
from unittest.mock import MagicMock

# Mock pydantic before importing the app if needed, but fastapi will pull it anyway.
import backend.main as main_app

client = TestClient(main_app.app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

def test_capture_stream_unauthenticated():
    response = client.post("/api/v1/capture/stream", params={"user_id": "test_user"})
    # HTTPBearer returns 403 when Authorization header is completely missing in some versions
    assert response.status_code in [401, 403]

def test_capture_stream_authenticated_missing_env(monkeypatch):
    monkeypatch.delenv("GUCE_API_KEY", raising=False)
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer some_token"}
    )
    assert response.status_code == 500

def test_capture_stream_authenticated_invalid_token(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_token")
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer wrong_token"}
    )
    assert response.status_code == 401

def test_capture_stream_authenticated_valid_token(monkeypatch):
    monkeypatch.setenv("GUCE_API_KEY", "correct_token")
    response = client.post(
        "/api/v1/capture/stream",
        params={"user_id": "test_user"},
        headers={"Authorization": "Bearer correct_token"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "STREAMING"
