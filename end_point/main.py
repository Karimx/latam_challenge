import pickle
#import redis
import json

from fastapi import FastAPI

from end_point.schemas.features import PredictionInput

app = FastAPI()
cache = redis.Redis(host='localhost', port=6379)

with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.post("/predict")
async def predict(input: PredictionInput):
    # Convert input to a numpy array
    input_array = [[input.feature1, input.feature2, input.feature3]]

    # Check if input values are already cached
    cached_prediction = cache.get(json.dumps(input_array))
    if cached_prediction is not None:
        prediction = float(cached_prediction.decode('utf-8'))
    else:
        # Make a prediction using the loaded model
        prediction = model.predict(input_array)[0]

        # Store prediction in cache
        cache.set(json.dumps(input_array), str(prediction))

    # Return the prediction
    return {"prediction": prediction}