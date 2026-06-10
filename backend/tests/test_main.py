from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "4.0.0"}

def test_start_capture_stream():
    response = client.post("/api/v1/capture/stream?user_id=123")
    assert response.status_code == 200
    assert response.json()["user_id"] == "123"
    assert response.json()["status"] == "STREAMING"


def test_optimize_tensor_stream_no_auth():
    response = client.post("/api/v1/tensor-stream/optimize")
    assert response.status_code in [401, 403]

def test_optimize_tensor_stream_missing_env(monkeypatch):
    monkeypatch.delenv("TENSOR_STREAM_API_KEY", raising=False)
    response = client.post("/api/v1/tensor-stream/optimize", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 500

def test_optimize_tensor_stream_invalid_key(monkeypatch):
    monkeypatch.setenv("TENSOR_STREAM_API_KEY", "correct_key")
    response = client.post("/api/v1/tensor-stream/optimize", headers={"Authorization": "Bearer wrong_key"})
    assert response.status_code == 401

def test_optimize_tensor_stream_valid_key(monkeypatch):
    monkeypatch.setenv("TENSOR_STREAM_API_KEY", "correct_key")
    response = client.post("/api/v1/tensor-stream/optimize", headers={"Authorization": "Bearer correct_key"})
    assert response.status_code == 200
    assert response.json() == {"optimization": "complete", "stream": "tensorized"}
