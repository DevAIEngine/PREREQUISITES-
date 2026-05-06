import pytest
import os
import sys
from fastapi.testclient import TestClient

# Mock missing dependencies
from unittest.mock import MagicMock
import sys

sys.path.insert(0, os.path.abspath("backend"))

from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

def test_capture_stream_no_auth():
    response = client.post("/api/v1/capture/stream?user_id=123")
    assert response.status_code in [401, 403]

def test_capture_stream_invalid_auth():
    os.environ["GUCE_API_KEY"] = "secret"
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer bad_secret"})
    assert response.status_code == 401

def test_capture_stream_valid_auth():
    os.environ["GUCE_API_KEY"] = "secret"
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer secret"})
    assert response.status_code == 200
    assert response.json()["user_id"] == "123"

def test_capture_stream_missing_env_var():
    if "GUCE_API_KEY" in os.environ:
        del os.environ["GUCE_API_KEY"]
    response = client.post("/api/v1/capture/stream?user_id=123", headers={"Authorization": "Bearer secret"})
    assert response.status_code == 500
