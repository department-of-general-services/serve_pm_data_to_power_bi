from datetime import datetime
from pickle import OBJ
import pandas as pd
from pm_stats.utils.constants import (
    COLUMN_MAPPING,
    BOOL_COLS,
    DATE_COLS,
    FLOAT_COLS,
    INT_COLS,
    OBJECT_COLS,
)


def rename(df: pd.DataFrame, mapping=COLUMN_MAPPING) -> pd.DataFrame:
    return df.rename(columns=COLUMN_MAPPING)


def cast_init_types(df: pd.DataFrame) -> pd.DataFrame:
    df[OBJECT_COLS] = df[OBJECT_COLS].astype(str)
    df[INT_COLS] = df[INT_COLS].astype("Int64")
    df[FLOAT_COLS] = df[FLOAT_COLS].astype(float)
    df[DATE_COLS] = df[DATE_COLS].astype("datetime64[ns]")
    df[BOOL_COLS] = df[BOOL_COLS].astype(bool)
    return df


def cast_types(df: pd.DataFrame) -> pd.DataFrame:
    mapper = {"Y": 1, "N": 0}
    df[["is_off_schedule", "is_on_schedule"]] = df[
        ["is_off_schedule", "is_on_schedule"]
    ].replace(mapper)
    df[["is_off_schedule", "is_on_schedule"]] = df[
        ["is_off_schedule", "is_on_schedule"]
    ].astype(bool)
    return df


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = rename(df)
    df = cast_init_types(df)
    df = cast_types(df)
    return df
