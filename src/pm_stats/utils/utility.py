# pylint: disable=C0103
import pandas as pd
import numpy as np
from pm_stats.systems.faster.models import (
    BOOL_COLS,
    DATE_COLS,
    FLOAT_COLS,
    INT_COLS,
    OBJECT_COLS,
)


def rename_cols(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """Renames the columns of the dataframe according to a
    dictionary with mapping.

    Args:
        df (pd.DataFrame): Input dataframe
        mapping (dict): Key-value pairs with name-change instructions

    Returns:
        pd.DataFrame: Output dataframe
    """
    df = df.copy()
    return df.rename(columns=mapping)


def cast_init_types(df: pd.DataFrame) -> pd.DataFrame:
    """Sets initial types for work orders data returned by
    the stored procedure in Faster.

    Args:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Output dataframe
    """
    df = df.copy()
    df[OBJECT_COLS] = df[OBJECT_COLS].fillna("").astype(str)
    df[INT_COLS] = df[INT_COLS].astype("Int64")
    df[FLOAT_COLS] = df[FLOAT_COLS].astype(float)
    df[DATE_COLS] = df[DATE_COLS].astype("datetime64[ns]")
    df[BOOL_COLS] = df[BOOL_COLS].astype(bool)
    return df


def replace_values(df: pd.DataFrame) -> pd.DataFrame:
    """Replaces values to allow consistent typing.

    Args:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Output dataframe
    """
    df = df.copy()
    mapper = {"Y": 1, "N": 0, "": 0}
    df[["road_call", "accident"]] = df[["road_call", "accident"]].replace(
        mapper
    )
    return df


def compute_weeks_late(df: pd.DataFrame) -> pd.DataFrame:
    """Converts the days_late column to weeks, which are more
    appropriate for communicating with agencies. 

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = df.copy()
    df["weeks_late"] = df["days_late"].astype(
        "timedelta64[D]"
    ) / np.timedelta64(1, "W")
    return df


def cast_types(df: pd.DataFrame) -> pd.DataFrame:
    """After initial type-casting and value replacement, we have
    a bit more to do to get the adjusted data cast to
    the right types.

    Args:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Output dataframe
    """
    df = df.copy()
    df[["is_off_schedule", "is_on_schedule"]] = df[
        ["is_off_schedule", "is_on_schedule"]
    ].astype(bool)
    return df


def prepare_data(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """Runs all data-preparation functions in sequence to
    complete workflow.

    Args:
        df (pd.DataFrame): Input dataframe
        mapping (dict): Output dataframe

    Returns:
        pd.DataFrame: _description_
    """
    df = df.copy()
    df = compute_weeks_late(df)
    df = rename_cols(df, mapping=mapping)
    df = cast_init_types(df)
    df = replace_values(df)

    df = cast_types(df)
    return df
