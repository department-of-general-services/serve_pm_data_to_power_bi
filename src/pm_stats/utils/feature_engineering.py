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


def compute_days_in_service(df: pd.DataFrame) -> pd.DataFrame:
    """Computes the age of the vehicle by computing the number of days
    between today's date and the date of the vehicle's acquisition.

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.copy()
    current_date = datetime.now()
    df["vehicle_days_in_service"] = (
        current_date - df["acquire_date"]
    ) / np.timedelta64(1, "D")
    return df


def engineer_features(assets: pd.DataFrame) -> pd.DataFrame:
    """Full docstring to come"""
    assets = assets.copy()
    assets = compute_vehicle_age(assets)
    assets = compute_days_in_service(assets)
    return assets
