import pandas as pd

from pm_stats.utils.aggregations import (
    aggregate_wos_to_assets,
    merge_with_asset_details,
    rename_asset_cols,
)
from pm_stats.systems.faster import prepared_wo_table, raw_asset_details_table
from pm_stats.utils.constants import (
    AGG_MAPPING,
    AGG_RENAMING,
    VEHICLE_ATTRIBUTES,
)


class TestAggregateWOsToAssets:
    """Class for testing the aggregate_wos_to_assets function"""

    def test_rename_cols_is_function(self):
        """Tests that the aggregate_wos_to_assets function is a function"""
        assert callable(aggregate_wos_to_assets)

    def test_aggregation_gets_right_row_count(self):
        """Tests that the aggregate_wos_to_assets function gets the right number
        of assets when aggregating."""
        # setup
        expected_length = 2
        work_orders = pd.DataFrame.from_dict(prepared_wo_table, orient="index")
        # execution
        assets = aggregate_wos_to_assets(
            work_orders, AGG_MAPPING, VEHICLE_ATTRIBUTES
        )
        # validation
        assert len(assets) == expected_length

    # def test_aggregation_provides_expected_columns(self):
    #     # setup
    #     # expected_length = 2
    #     # work_orders = pd.DataFrame.from_dict(prepared_wo_table, orient="index")
    #     # execution
    #     # assets = aggregate_wos_to_assets(work_orders, AGG_MAPPING, VEHICLE_ATTRIBUTES)
    #     # validation
    #     assert 1


class TestMergeWithAssetDetails:
    """Class for testing the merge_with_asset_details function"""

    def test_merge_with_asset_details_is_function(self):
        """Tests that the merge_with_asset_details function is a function"""
        assert callable(merge_with_asset_details)

    def test_merge_with_asset_details_gets_correct_columns(self, test_assets: pd.DataFrame):
        """Tests that the merge_with_asset_details function adds the new columns we expect"""
        # setup
        assets = test_assets
        asset_details = pd.DataFrame.from_dict(
            raw_asset_details_table, orient="index"
        )
        # execution
        merged = merge_with_asset_details(assets, asset_details)
        # validation
        assert len(merged.columns) > len(assets.columns)


class TestRenameAssetCols:
    """Class for testing the rename_asset_cols function"""

    def test_rename_asset_cols_is_function(self):
        """Tests that the rename_asset_cols function is a function"""
        assert callable(rename_asset_cols)

    def test_rename_asset_cols_provides_correct_cols(
        self, test_merged_assets: pd.DataFrame
    ):
        """Tests that the rename_asset_cols function outputs
        a dataframe with the expected columns"""
        # setup
        merged = test_merged_assets
        expected_cols = list(AGG_RENAMING.values()) + VEHICLE_ATTRIBUTES
        # execution
        renamed = rename_asset_cols(merged, mapping=AGG_RENAMING)
        assert sorted(renamed.columns) == sorted(expected_cols)
