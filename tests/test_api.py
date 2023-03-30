import pytest
from fastapi.testclient import TestClient

from end_point.main import app

client = TestClient(app)


def test_predict_endpoint():
    d = {'operator': 'Grupo LATAM', 'flight_type': 'I', 'month': '11'}
    response = client.post('/predict/', json=d)
    assert response.status_code == 200
    response = client.post('/predict/', json=d)
    assert response.status_code == 200
    print(response.json())
    # assert response.json() == {"item_id": 42, "item_name": "Test Item"}
    # ?skip=5&limit=20


async def test_retraining_endpoint():
    response = client.post('/retrain/')
    assert response.status_code == 200
    # assert response.json() == {"item_id": 42, "item_name": "Test Item"}


@pytest.mark.asyncio
async def test_stress_on_predict():
    import time

    start_time = time.perf_counter()
    d = {'operator': 'Grupo LATAM', 'flight_type': 'I', 'month': '11'}
    for i in range(100):
        response = client.post('/predict/', json=d)
        assert response.status_code == 200
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'Elapsed time: {elapsed_time:.2f} seconds')
    # 5k Elapsed time: 16.01 seconds
    # 10k Elapsed time: 42.09 seconds
    # 10k Elapsed time: 35.09 seconds with ancyio
    # 10k Elapsed time: 31.53 seconds with ancyio, model default
    # 34.02 model chaded decorator
    # locust -f locustfile.py --host=http://localhost:8000
    #  50.000 requests durante 45 segundos.


@pytest.mark.asyncio
async def test_stress_on_cached_predict():
    import time

    start_time = time.perf_counter()
    d = {'operator': 'Grupo LATAM', 'flight_type': 'I', 'month': '11'}
    for i in range(20000):
        response = client.post('/predict_cache/', json=d)
        # assert response.status_code == 200
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'Elapsed time: {elapsed_time:.2f} seconds')
