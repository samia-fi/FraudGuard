
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_score_transaction_below_maximum():
    payload = {
        "transaction_id": "550e8400-e29b-41d4-a716-446655440000",
        "merchant_id": "550e8400-e29b-41d4-a716-446655440001",
        "amount": 250.50,
        "currency": "MAD",
    }

    response = client.post(
        "/api/v1/transactions/score",
        json=payload,
    )

    assert response.status_code == 200
    assert response.json()["status"] == "REVIEW"


def test_score_transaction_above_maximum():
    payload = {
        "transaction_id": "550e8400-e29b-41d4-a716-446655440000",
        "merchant_id": "550e8400-e29b-41d4-a716-446655440001",
        "amount": 15000,
        "currency": "MAD",
    }

    response = client.post(
        "/api/v1/transactions/score",
        json=payload,
    )

    assert response.status_code == 200
    assert response.json()["status"] == "REJECT"


def test_score_transaction_with_negative_amount():
    payload = {
        "transaction_id": "550e8400-e29b-41d4-a716-446655440000",
        "merchant_id": "550e8400-e29b-41d4-a716-446655440001",
        "amount": -50,
        "currency": "MAD",
    }

    response = client.post(
        "/api/v1/transactions/score",
        json=payload,
    )

    assert response.status_code == 422
