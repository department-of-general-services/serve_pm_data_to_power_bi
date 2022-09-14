import pandas as pd
import pytest

from src.pm_stats.systems.faster import Faster
from tests.testing_utils.work_orders_data import raw_work_order_table


@pytest.fixture(scope="function", name="test_faster")
def raw_work_orders() -> pd.DataFrame:
    """Creates a mockup of the raw work orders dataset with only two rows for testing.

    Returns:
        pd.DataFrame: Mocked up dataset
    """
    data = pd.DataFrame.from_dict(raw_work_order_table, orient="index")
    test_faster = Faster(testing_data=data)
    return test_faster
