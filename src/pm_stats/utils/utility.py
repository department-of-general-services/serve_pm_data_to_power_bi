from pathlib import Path
import pandas as pd
import numpy as np
import yaml
from pm_stats.systems.faster.models import (
    BOOL_COLS,
    DATE_COLS,
    FLOAT_COLS,
    INT_COLS,
    OBJECT_COLS,
)


def load_experiments(experiments_path: Path) -> dict:
    """Reads the experiments configuration file from YAML format
    and renders it as a dictionary.

    Args:
        experiments_path (Path): The path to the YAML file

    Returns:
        dict: Python dictionary containing instructions for how to run the experiment
    """
    with open(experiments_path, "rt", encoding="utf-8") as file:
        experiments = yaml.safe_load(file)
        return experiments


def rename_cols(work_orders: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """Renames the columns of the dataframe according to a
    dictionary with mapping.

    Args:
        work_orders (pd.DataFrame): Input dataframe
        mapping (dict): Key-value pairs with name-change instructions

    Returns:
        pd.DataFrame: Output dataframe
    """
    work_orders = work_orders.copy()
    return work_orders.rename(columns=mapping)


def cast_init_types(work_orders: pd.DataFrame) -> pd.DataFrame:
    """Sets initial types for work orders data returned by
    the stored procedure in Faster.

    Args:
        work_orders (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Output dataframe
    """
    work_orders = work_orders.copy()
    work_orders[OBJECT_COLS] = work_orders[OBJECT_COLS].fillna("").astype(str)
    work_orders[INT_COLS] = work_orders[INT_COLS].astype("Int64")
    work_orders[FLOAT_COLS] = work_orders[FLOAT_COLS].astype(float)
    work_orders[DATE_COLS] = work_orders[DATE_COLS].astype("datetime64[ns]")
    work_orders[BOOL_COLS] = work_orders[BOOL_COLS].astype(bool)
    return work_orders


def replace_values(work_orders: pd.DataFrame) -> pd.DataFrame:
    """Replaces values to allow consistent typing.

    Args:
        work_orders (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Output dataframe
    """
    work_orders = work_orders.copy()
    mapper = {"Y": 1, "N": 0, "": 0}
    work_orders[["road_call", "accident"]] = work_orders[["road_call", "accident"]].replace(
        mapper
    )
    return work_orders


def compute_weeks_late(work_orders: pd.DataFrame) -> pd.DataFrame:
    """Converts the days_late column to weeks, which are more
    appropriate for communicating with agencies.

    Args:
        work_orders (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    work_orders = work_orders.copy()
    work_orders["weeks_late"] = work_orders["days_late"].astype(
        "timedelta64[D]"
    ) / np.timedelta64(1, "W")
    return work_orders


def cast_types(work_orders: pd.DataFrame) -> pd.DataFrame:
    """After initial type-casting and value replacement, we have
    a bit more to do to get the adjusted data cast to
    the right types.

    Args:
        work_orders (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Output dataframe
    """
    work_orders = work_orders.copy()
    work_orders[["is_off_schedule", "is_on_schedule", "accident", "road_call"]] = work_orders[
        ["is_off_schedule", "is_on_schedule", "accident", "road_call"]
    ].astype(bool)
    return work_orders


def drop_accidents(work_orders: pd.DataFrame) -> pd.DataFrame:
    """Drops work orders including an accident

    Args:
        work_orders (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    return work_orders[~work_orders["accident"]]


def prepare_data(work_orders: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """Runs all data-preparation functions in sequence to
    complete workflow.

    Args:
        work_orders (pd.DataFrame): Input dataframe
        mapping (dict): Output dataframe

    Returns:
        pd.DataFrame: _description_
    """
    work_orders = work_orders.copy()
    work_orders = rename_cols(work_orders, mapping=mapping)
    work_orders = cast_init_types(work_orders)
    work_orders = replace_values(work_orders)
    work_orders = cast_types(work_orders)
    work_orders = compute_weeks_late(work_orders)
    work_orders = drop_accidents(work_orders)
    return work_orders
