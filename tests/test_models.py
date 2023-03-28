from inference_server.models import airport_delay_model
import numpy as np


def test_plain_inference():
    model = airport_delay_model()
    input_shape = model.feats_in
    randnums = np.random.randint(0, 2, size=input_shape)
    r= model(np.reshape(randnums, (1, -1)))
    print(r)


def test_model_predict():
    sample = ['sky airline', 'I', '8']
    model = airport_delay_model()
    #input_shape = model.feats_in
    #randnums = np.random.randint(0, 2, size=input_shape)
    r=model.predict(sample)
    print(r)



