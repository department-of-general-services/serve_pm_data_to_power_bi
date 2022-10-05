import pandas as pd
import pytest

from pm_stats.systems.faster import (
    Faster,
    raw_wo_table,
    raw_asset_details_table,
    prepared_wo_table,
)
from pm_stats.utils import aggregate_wos_to_assets, merge_with_asset_details
from pm_stats.utils.constants import AGG_MAPPING, VEHICLE_ATTRIBUTES


@pytest.fixture(scope="function", name="test_faster")
def create_test_faster() -> Faster:
    """Creates a mockup of the raw work orders dataset with only two rows for testing.

    Returns:
        Faster: An object of class Faster, with the raw work orders stored as an attribute.
    """
    work_orders = pd.DataFrame.from_dict(raw_wo_table, orient="index")
    test_faster = Faster(testing_data=work_orders)
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


@pytest.fixture(scope="function", name="test_merged_assets")
def create_test_merged_assets() -> pd.DataFrame:
    """Creates a mockup of the raw work orders dataset with only two rows for testing.

    Returns:
        pd.DataFrame: Mocked up dataset
    """
    work_orders = pd.DataFrame.from_dict(prepared_wo_table, orient="index")
    assets = aggregate_wos_to_assets(
        work_orders, AGG_MAPPING, VEHICLE_ATTRIBUTES
    )
    asset_details = pd.DataFrame.from_dict(
        raw_asset_details_table, orient="index"
    )
    return merge_with_asset_details(assets, asset_details)
