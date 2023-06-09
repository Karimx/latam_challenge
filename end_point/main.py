import json

from fastapi import FastAPI

from end_point.schemas.features import PredictionInput, TipoVuelo, operators
from end_point.service import predict_delay_15
from resources.cache import redis_db

app = FastAPI()


@app.post('/predict/')
async def predict(input_: PredictionInput):
    """

    Args:
        input_: input_: operator: str  # o poner int?
                flight_type: TipoVuelo
                month: Mes
                proba: bool = True

    Returns: when proba = True, retrieve probability delay is more than 15 minutes

    """
    if input_.operator.lower() not in operators:
        return {'error': f'Airline operato must be {operators}'}
    if 1 <= int(input_.month) <= 12:
        return {'error': f'Number month incorrect [1-12]'}
    if input_.flight_type.upper() not in list(TipoVuelo):
        return {'error': f'Type of flight not accepted'}
    result = predict_delay_15(
        [input_.operator, str(input_.flight_type), str(input_.month)]
    )
    result = result[0]
    return {'delay': result[1], 'no_delay': result[0]}


@app.post('/retrain/')
async def retrain():
    """manually activate retrain pipeline

    Returns: status code

    """
    return {'status': 200}


@app.post('/predict_cache/')
async def predict_cache(input_: PredictionInput):
    """

    Args:
        input_: operator: str  # o poner int?
                flight_type: TipoVuelo
                month: Mes
                proba: bool = True

    Returns: when proba = True, retrieve probability delay is more than 15 minutes, else both return an array with both

    """
    in_data = [input_.operator, str(input_.flight_type), str(input_.month)]
    cached_prediction = redis_db.get(json.dumps(in_data))

    if cached_prediction is not None:
        prediction = cached_prediction.decode('utf-8')
    else:
        prediction = predict_delay_15(
            [input_.operator, str(input_.flight_type), str(input_.month)]
        )
        redis_db.set(json.dumps(in_data), str(prediction))
    return {'prediction': prediction}


@app.get('/predict_test/')
async def predict_sample():
    """sample prediction end-point to perform stress test

    Returns:

    """
    sample = ['sky airline', 'I', '8']
    result = predict_delay_15(sample)
    result = result[0]
    return {'delay': result[1], 'no_delay': result[0]}


@app.get('/predict_cache_test/')
async def predict_sample_cache():
    """sample prediction end-point to perform stress test, uses a redis database as cache

    Returns:

    """
    sample = ['sky airline', 'I', '9']
    cached_prediction = redis_db.get(json.dumps(sample))
    if cached_prediction is not None:
        prediction = cached_prediction.decode('utf-8')
    else:
        prediction = predict_delay_15(sample)
        redis_db.set(json.dumps(sample), str(prediction))
    return {'prediction': prediction}


@app.get('/')
async def home():
    return {'message': 'Welcome to Model performance api'}
