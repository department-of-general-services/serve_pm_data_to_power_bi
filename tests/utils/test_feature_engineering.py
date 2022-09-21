from typing import List
from datetime import datetime
import pandas as pd

from pm_stats.utils import compute_vehicle_age

# from pm_stats.systems.faster import prepared_wo_table
from pm_stats.utils.constants import VEHICLE_ATTRIBUTES


class TestComputeVehicleAge:
    """Class for testing the compute_vehicle_age function"""

    def test_rename_cols_is_function(self):
        """Tests that the compute_vehicle_age function is a function"""
        assert callable(compute_vehicle_age)

    def test_compute_vehicle_age_gets_correct_ages(
        self, test_assets: pd.DataFrame
    ):
        """Tests that the compute_vehicle_age function gets the right ages for the two
        vehicles in the testing data"""
        # setup
        expected = {
            "012": {"vehicle_age": datetime.now().year - 2012},
            "013": {"vehicle_age": datetime.now().year - 2013},
        }
        # execution
        result = (
            compute_vehicle_age(test_assets)
            .set_index("asset_number")[["vehicle_age"]]
            .to_dict("index")
        )
        # validation
        assert result == expected

    def test_compute_vehicle_age_contains_expected_cols(
        self,
        test_assets: pd.DataFrame,
    ):
        """Tests that a subset of expected columns at the asset level
        (that is, the ones that don't require aggregation) all exist in
        the assets dataframe.

        Args:
            test_assets (pd.DataFrame): Fixture with asset-level data
        """
        # setup
        expected_cols: List[str] = VEHICLE_ATTRIBUTES
        # validation
        assert all(col in test_assets.columns for col in expected_cols)
