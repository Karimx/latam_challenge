from functools import wraps

from loguru import logger

from inference_server.models import airport_delay_model

__all__ = ["predict_delay_15"]

def model_cache(func):
    @wraps(func)
    def cached(*args, **kwargs):
        if not hasattr(func, "model"):
            func.model = airport_delay_model()
            logger.info("Model Loaded and cached")
        return func(*args, **kwargs)
    return cached


@model_cache
def predict_delay_15(inputs: list): #model=airport_delay_model()):
    model = airport_delay_model()
    return model.predict(inputs)
