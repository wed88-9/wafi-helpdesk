from fastapi.testclient import TestClient

from src.api.main import app


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready():
    with TestClient(app) as client:
        response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_predict_valid_request():
    with TestClient(app) as client:
        response = client.post(
            "/v1/predict",
            json={"text": "All employees cannot access the system"},
        )

    assert response.status_code == 200

    body = response.json()

    assert "trace_id" in body
    assert body["data"]["team"] == "IT Support"
    assert body["data"]["urgency"] == "urgent"


def test_predict_rejects_short_text():
    with TestClient(app) as client:
        response = client.post(
            "/v1/predict",
            json={"text": "Hi"},
        )

    assert response.status_code == 422


def test_predict_rejects_unknown_fields():
    with TestClient(app) as client:
        response = client.post(
            "/v1/predict",
            json={
                "text": "I forgot my password",
                "extra": "not allowed",
            },
        )

    assert response.status_code == 422
