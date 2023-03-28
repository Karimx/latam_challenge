from fastapi.testclient import TestClient
from end_point.main import app

client = TestClient(app)


def test_predict_endpoint():
    response = client.get("/predict/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "item_name": "Test Item"}


def test_retraining_endpoint():
    response = client.get("/retrain/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "item_name": "Test Item"}
