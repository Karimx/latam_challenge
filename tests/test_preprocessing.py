from pathlib import Path

from end_point.schemas.features import Mes, TipoVuelo, operators
from inference_server.feature_mgn.features import (Categorical, FeaturesGroup,
                                                   OneHotEncoder)
from inference_server.inference.core import Preprocessing


def preprocessing_test():
    operators
    TipoVuelo
    Mes
    Preprocessing()


def test_feature_can_decode_onehotmap():
    f = Path('../inference_server/feature_storage/hotmap_operator.json')
    operator_feat = Categorical(OneHotEncoder(f))
    print(operator_feat.encode(operators[0]))
    assert sum(operator_feat.encode(operators[0])) == 1
    assert operator_feat.hash(operators[1])
    assert operator_feat.keys()


def test_feature_group_encode():
    f = Path('../inference_server/feature_storage/hotmap_operator.json')
    feat1 = Categorical(OneHotEncoder(f))
    feat2 = Categorical(OneHotEncoder(f))
    fg = FeaturesGroup([feat1, feat2])
    enc = fg.encode([operators[0], operators[0]])
    assert sum(enc) == 2
    assert fg.hash([operators[0], operators[0]])
    print(enc)
    print(len(enc))
    print(fg.hash([operators[0], operators[0]]))




import numpy as np


class Tee:
    def __init__(self):
        self.data = [list(range(10)), list(range(2)), list(range(100, 105))]

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        pass

    def array(self):
        a = np.array([*self.data])
        return np.concatenate(a, axis=0)

def test_t():
    t = Tee()
    print(t.array() )


