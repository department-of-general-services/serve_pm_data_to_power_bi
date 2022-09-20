import pandas as pd
import pytest

from pm_stats.systems.faster import Faster, raw_wo_table, prepared_wo_table
from pm_stats.utils import (
    aggregate_wos_to_assets,
    AGG_MAPPING,
    VEHICLE_ATTRIBUTES,
)


@pytest.fixture(scope="function", name="test_faster")
def create_test_faster() -> Faster:
    """Creates a mockup of the raw work orders dataset with only two rows for testing.

    Returns:
        Faster: An object of class Faster, with the raw work orders stored as an attribute.
    """
    data = pd.DataFrame.from_dict(raw_wo_table, orient="index")
    test_faster = Faster(
        asset_profile="caprice_1_month_cycle", testing_data=data
    )
    return test_faster


@pytest.fixture(scope="function", name="test_assets")
def create_test_assets() -> pd.DataFrame:
    """Creates a mockup of the raw work orders dataset with only two rows for testing.

    Returns:
        pd.DataFrame: Mocked up dataset
    """
    work_orders = pd.DataFrame.from_dict(prepared_wo_table, orient="index")
    assets = aggregate_wos_to_assets(
        work_orders, AGG_MAPPING, VEHICLE_ATTRIBUTES
    )
    return assets
