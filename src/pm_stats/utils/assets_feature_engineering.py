# pylint: disable = "invalid-name"
from datetime import datetime
import pandas as pd
import numpy as np


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


def compute_duration_in_service(df: pd.DataFrame) -> pd.DataFrame:
    """Computes the age of the vehicle by computing the number of years
    between the date of the vehicle's acquisition and today's date.

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.copy()
    date_of_first_work_order = df["first_completion_date"]
    df["vehicle_years_in_service"] = (
        date_of_first_work_order - df["acquire_date"]
    ) / np.timedelta64(1, "Y")

    return df


def engineer_asset_features(assets: pd.DataFrame) -> pd.DataFrame:
    """Full docstring to come"""
    assets = assets.copy()
    assets = compute_vehicle_age(assets)
    assets = compute_duration_in_service(assets)
    return assets
