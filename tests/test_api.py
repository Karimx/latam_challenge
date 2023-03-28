from fastapi.testclient import TestClient
from end_point.main import app

client = TestClient(app)


def test_predict_endpoint():
    response = client.get("/predict/proba: ")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "item_name": "Test Item"}


def test_retraining_endpoint():
    response = client.get("/retrain/")
    assert response.status_code == 200
    #assert response.json() == {"item_id": 42, "item_name": "Test Item"}
