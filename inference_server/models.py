from inference_server.inference.core import BinaryClassification, Preprocessing
from inference_server.model_store import KeyMetadata, model_repo


def airport_delay_model():
    """configure and load weights

    Returns: airport delay 15m model

    """
    d = model_repo('delay_15')
    return BinaryClassification(
        d[KeyMetadata.SHAPE],
        d[KeyMetadata.WEIGHTS],
        Preprocessing(d[KeyMetadata.TEMPLATE]),
        d[KeyMetadata.NAME],
    )
