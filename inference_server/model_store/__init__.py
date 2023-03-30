from enum import Enum
from pathlib import Path

from inference_server.model_store.input_templates import \
    airport_delay_15_template

delay_15_weights = Path('log_delay_15.pkl')


class KeyMetadata(str, Enum):
    NAME = ('name',)
    WEIGHTS = 'weights'
    TEMPLATE = 'input_template'
    SHAPE = 'input_shape'


delay_15_metadata = {
    'name': 'delay_15',
    'weights': delay_15_weights,
    'input_template': airport_delay_15_template(),
    'input_shape': (1, 37),
}

models = {
    delay_15_metadata['name']: delay_15_metadata,
}


def model_repo(name: str):
    return models[name]
