import pickle
#import redis
import json

from fastapi import FastAPI

from end_point.schemas.features import PredictionInput
from end_point.service import predict_delay_15


app = FastAPI()


@app.post("/predict/")
async def predict(input_: PredictionInput):
    result = predict_delay_15([input_.operator, str(input_.flight_type), str(input_.month)])
    # todo error handler
    return {"prediction": result}

@app.post("/retrain/")
async def retrain():
    return {"status": 200}
