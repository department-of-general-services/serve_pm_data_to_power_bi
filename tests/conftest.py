import pandas as pd
import pytest

from pm_stats.systems.faster import Faster, raw_wo_table


@pytest.fixture(scope="function", name="test_faster")
def raw_work_orders() -> pd.DataFrame:
    """Creates a mockup of the raw work orders dataset with only two rows for testing.

    Returns:
        pd.DataFrame: Mocked up dataset
    """
    data = pd.DataFrame.from_dict(raw_wo_table, orient="index")
    test_faster = Faster(testing_data=data)
    return test_faster
