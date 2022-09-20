# pylint: disable = "invalid-name"
import pandas as pd


def compute_vehicle_general_age(df: pd.DataFrame) -> pd.DataFrame:
    """Computes the age of the vehicle in the simplest sense,
    measured as today's year minus the year of the vehicle's make.

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.copy()
    return df
