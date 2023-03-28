from pathlib import Path
from typing import List, NamedTuple, Protocol

from inference_server.feature_mgn.features import (FeatConfig, FeatType,
                                                   OneHotEncoder)

root = Path(__file__).parent.resolve()
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

def airport_delay_15_template() -> List[FeatConfig]:
    from pathlib import Path

    operator_feat = FeatConfig(name='operator', feat_type=FeatType.Categorical, transform = OneHotEncoder(root.joinpath(Path('../feature_storage/hotmap_operator.json'))), output_len=23)
    flight_feat = FeatConfig(name='flight_type', feat_type=FeatType.Categorical, transform=OneHotEncoder(root.joinpath('../feature_storage/onehot_flight_type.json')), output_len=2)
    mount_feat = FeatConfig(name='month', feat_type= FeatType.Categorical, transform=OneHotEncoder(root.joinpath('../feature_storage/onehot_date.json')), output_len=12)

    return [operator_feat, flight_feat, mount_feat]

