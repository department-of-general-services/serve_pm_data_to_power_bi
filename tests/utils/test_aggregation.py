import pandas as pd

from pm_stats.utils import aggregate_wos_to_assets


class TestAggregateWOsToAssets:
    """Class for testing the aggregate_wos_to_assets function"""

    def test_rename_cols_is_function(self):
        """Tests that the rename_cols function is a function"""
        assert callable(aggregate_wos_to_assets)

    def test_aggregation_gets_right_row_count(self):
        """Tests that the rename_cols function transforms column names into
        expected form."""
        # setup

        # execution

        # validation
        assert 1
