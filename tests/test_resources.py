from inference_server.models import airport_delay_model
from resources.cache import redis_db
import json


def test_cache_connection():
    sample = ['sky airline', 'I', '8']
    cached_prediction = redis_db.get(json.dumps(sample))
    model = airport_delay_model()

    if cached_prediction is not None:
        prediction = cached_prediction.decode('utf-8')
        print("from cache")
    else:
        prediction = model.predict(sample)
        redis_db.set(json.dumps(sample), str(prediction))

    print(f"prediction {prediction}")
    cached_prediction = redis_db.get(json.dumps(sample))

    print(f"cached {cached_prediction}")
    assert cached_prediction is not None
    # return {"prediction": result}
#   redict_delay_15([input_.operator, str(input_.flight_type), str(input_.month)])
