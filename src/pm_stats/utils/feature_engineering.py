# pylint: disable = "invalid-name"
from datetime import datetime
import pandas as pd


def compute_vehicle_age(df: pd.DataFrame) -> pd.DataFrame:
    """Computes the age of the vehicle in the simplest sense,
    measured as today's year minus the year of the vehicle's make.

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.copy()
    current_year = datetime.now().year
    df["vehicle_age"] = (current_year - df["vehicle_year"]).astype(int)
    return df


def rename_cols_in_assets_table(
    df: pd.DataFrame, mapping: dict
) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        mapping (dict): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.copy()
    return df
