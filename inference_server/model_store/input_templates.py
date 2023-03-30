from pathlib import Path
from typing import List

from inference_server.feature_mgn.features import (FeatConfig, FeatType,
                                                   OneHotEncoder)

__all__ = ['airport_delay_15_template']

root = Path(__file__).parent.resolve()


def airport_delay_15_template() -> List[FeatConfig]:
    """Inputs tempate init and config for each required feature

    Returns: list of feature configurations

    """

    operator_feat = FeatConfig(
        name='operator',
        feat_type=FeatType.Categorical,
        transform=OneHotEncoder(
            root.joinpath(Path('../feature_storage/hotmap_operator.json'))
        ),
        output_len=23,
    )
    flight_feat = FeatConfig(
        name='flight_type',
        feat_type=FeatType.Categorical,
        transform=OneHotEncoder(
            root.joinpath('../feature_storage/onehot_flight_type.json')
        ),
        output_len=2,
    )
    mount_feat = FeatConfig(
        name='month',
        feat_type=FeatType.Categorical,
        transform=OneHotEncoder(
            root.joinpath('../feature_storage/onehot_date.json')
        ),
        output_len=12,
    )

    return [operator_feat, flight_feat, mount_feat]
