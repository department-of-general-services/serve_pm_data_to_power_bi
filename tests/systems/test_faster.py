import pandas as pd

from pm_stats.systems.faster import Faster


class TestFaster:
    """Unit tests for the Faster class"""

    def test_init(self, test_faster):
        """Tests that the test_faster was instantiated correctly"""
        # validation
        assert isinstance(test_faster, Faster)

    def test_faster_work_orders_is_dataframe(self, test_faster):
        """Tests that the test_faster was instantiated correctly"""
        # validation
        assert isinstance(test_faster.work_orders, pd.DataFrame)
