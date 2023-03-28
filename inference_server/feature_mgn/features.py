import json
from abc import abstractmethod
from enum import Enum
from typing import NamedTuple, Protocol, List


class Transform(Protocol):

    @abstractmethod
    def __call__(self, value):
        pass


class FeatType(Enum):
    Categorical = 0
    Continuous = 1


class FeatConfig(NamedTuple):
    name: str
    feat_type: FeatType
    transform: Transform
    output_len: int


class Feature:

    feat: FeatConfig

    def __call__(self, values):
        pass


class OneHotEncoder(Transform):

    def __init__(self, mapper):
        with open(mapper, 'r') as file:
            temp = json.load(file)
        self.data: dict = {k.lower(): v for k, v in temp.items()}

    def __call__(self, value):
        return self.data[value.lower()]

    def __getitem__(self, item):
        return self.data[item]

    def keys(self):
        return self.data.keys()


class IntEncoder:

    def __init__(self, mapper: str):
        with open(mapper, 'r') as file:
            temp = json.load(file)
        self.data: dict = {k.lower(): v for k, v in temp.items()}

    def __call__(self, value):
        return self.data[value.lower()]

    def __getitem__(self, item):
        return self.data[item]


class Categorical(Feature):

    def __init__(self, encoder: OneHotEncoder):
        self.f = encoder

        # with open(mapper, 'r') as file:
        #     temp = json.load(file)
        # self.data: dict = {k.lower(): v for k, v in temp.items()}

    def encode(self, value: str):
        return self.f(value)

    def keys(self):
        return self.f.keys()

    def hash(self, value: str):
        try:
            v = self.f.data[value]
        except KeyError:
            print("log no key found")
        return value.__hash__()

    def __str__(self):
        return f"{self.f}"

    def encodig(self):
        return len(self.f.data[0])

    def __len__(self):
        return len(self.f)

import numpy as np


class FeaturesGroup:

    def __init__(self, features: List[Categorical]):
        self.group = features

    def append(self, feature):
        self.group.append(feature)

    def __getitem__(self, item):
        return self.group[item]

    def __len__(self):
        return len(self.group)

    def encode(self, values: list):
        a = np.array([*[x.encode(y) for x, y in zip(self.group, values)]])
        return np.concatenate(a, axis=0)

    def hash(self, values):
        return hash(sum([x.hash(y) for x, y in zip(self.group, values)]))


