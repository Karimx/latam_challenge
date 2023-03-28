from pathlib import Path

import pickle
from enum import Enum

from typing import Protocol, Callable, List, Tuple, NamedTuple, Any

import numpy as np

from inference_server.feature_mgn.features import FeatConfig, FeatType, Categorical, FeaturesGroup
#from loader import load

#
# class Transform(Protocol):
#
#     def __call__(self):
#         pass
#
#
#
# class FeatType(Enum):
#     Categorical = 0
#     Continuous = 1
#
#
# class FeatConfig(NamedTuple):
#     name: str
#     feat_type: FeatType
#     transform: Transform
#     output_len: int
#
#
# class Feature:
#
#     feat: FeatConfig
#
#     def __call__(self, values):
#         pass
#
#
# def airport_delay_15_template() -> List[FeatConfig]:
#     operator_feat = FeatConfig(name='operator', feat_type=FeatType.Categorical, transform = OneHotEncoder('../inference_server/processing/hotmap_operator.json'), output_len=23)
#     flight_feat = FeatConfig('flight_type', FeatType.Categorical, OneHotEncoder(''), 2)
#     mount_feat = FeatConfig('month', FeatType.Categorical, OneHotEncoder(''), 12)
#     return [operator_feat, flight_feat, mount_feat]


class Preprocessing:

    def __init__(self,  template: List[FeatConfig]):
        self.fn = list(template)
        self.__features = []
        for f in self.fn:
            if f.feat_type == FeatType.Categorical:
                self.__features.append(Categorical( f.transform))

        self._fg = FeaturesGroup(self.__features)

    def __call__(self, input_features: list):
        return self._fg.encode(input_features)

    def hash(self, input_features: list):
        return self._fg.hash(input_features)


class ClassificationProtocol(Protocol):

    def predict(self, inputs: list) -> Any:
        pass


class BinaryClassification(ClassificationProtocol):

    def __init__(self, input_shape, weights, pre, name=None):
        self.feats_in = input_shape

        self.pre = pre

        loaded_model = pickle.load(open(Path(__file__).parent.joinpath('..','model_store', weights), 'rb'))
        self.model = loaded_model
        #self.model = load(weights)

    def predict(self, inputs: list) -> float:  # input squema
        f = self.pre(inputs)
        print(f)
        print(len(f))

        raw_result = self.model.predict_proba(np.reshape(f,(1, 37)))
        return raw_result

    def __call__(self, inputs: list) -> float:

        raw_result = self.model.predict_proba(inputs)
        return raw_result[1]




# ['OPERA', 'TIPOVUELO', 'MES']
# features =
# pd.concat([pd.get_dummies(data['OPERA'], prefix = 'OPERA'),pd.get_dummies(data['TIPOVUELO'], prefix = 'TIPOVUELO'), pd.get_dummies(data['MES'], prefix = 'MES')], axis = 1)
# label = data['atraso_15']
