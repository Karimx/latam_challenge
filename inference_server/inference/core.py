import pickle
from pathlib import Path
from typing import Any, List, Protocol

import numpy as np

from inference_server.feature_mgn.features import (Categorical, FeatConfig,
                                                   FeatType, FeaturesGroup)


class Preprocessing:
    """
        Preprocessing template executor
    """

    def __init__(self,  template: List[FeatConfig]):
        self.fn = list(template)
        self.__features = []
        for f in self.fn:
            if f.feat_type == FeatType.Categorical:
                self.__features.append(Categorical(f.transform))

        self._fg = FeaturesGroup(self.__features)

    def __call__(self, input_features: list):
        return self._fg.encode(input_features)

    def hash(self, input_features: list):
        """
            Returns a hash hashable input features
        Args:
            input_features:

        Returns: Hash of sum values

        """
        return self._fg.hash(input_features)


class ClassificationProtocol(Protocol):
    """
        Classifications task clase base
    """

    def predict(self, inputs: list) -> Any:
        """

        Args:
            inputs: raw features

        Returns: ouput model

        """
        pass


class BinaryClassification(ClassificationProtocol):
    """
        Concrete implementation of a binary classification wrapper
    """

    def __init__(self, input_shape, weights, pre, name=None):
        self.feats_in = input_shape
        self.pre = pre
        loaded_model = pickle.load(open(Path(__file__).parent.joinpath('..','model_store', weights), 'rb'))
        self.model = loaded_model


    def predict(self, inputs: list) -> float:  # input squema
        f = self.pre(inputs)
        raw_result = self.model.predict_proba(np.reshape(f,(1, 37)))
        return raw_result

    def __call__(self, inputs: list) -> float:
        raw_result = self.model.predict_proba(inputs)
        return raw_result[1]

