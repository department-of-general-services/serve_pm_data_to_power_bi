import pandas as pd

from pm_stats.utils import aggregate_wos_to_assets
from pm_stats.systems.faster import prepared_wo_table
from pm_stats.utils import AGG_MAPPING, VEHICLE_ATTRIBUTES


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
