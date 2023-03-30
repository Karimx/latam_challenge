import numpy as np

from inference_server.models import airport_delay_model


def test_plain_inference():
    model = airport_delay_model()
    input_shape = model.feats_in
    randnums = np.random.randint(0, 2, size=input_shape)
    inference = model(np.reshape(randnums, (1, -1)))
    assert len(inference) > 0


def test_model_predict():
    sample = ['sky airline', 'I', '8']
    model = airport_delay_model()
    r = model.predict(sample)
    assert len(r) > 0
