# pylint: disable=C0103
import pandas as pd
from pandas.api.types import (
    is_bool_dtype,
    is_object_dtype,
    is_int64_dtype,
    is_float_dtype,
    is_datetime64_dtype,
)
from pm_stats.utils import (
    # cast_types,
    cast_init_types,
    rename_cols,
    # prepare_data,
    replace_values,
)
from pm_stats.systems.faster import (
    COLUMN_MAPPING,
    OBJECT_COLS,
    INT_COLS,
    BOOL_COLS,
    FLOAT_COLS,
    DATE_COLS,
    intermediate_wo_table,
    raw_wo_table,
    prepared_wo_table,
)


class TestRenameCols:
    """Class for testing the rename function"""

    def test_rename_cols_is_function(self):
        """Tests that the rename_cols function is a function"""
        assert callable(rename_cols)

    def test_rename_cols_gets_right_columns(self):
        """Tests that the rename_cols function transforms column names into
        expected form."""
        # setup
        expected = pd.DataFrame.from_dict(prepared_wo_table, orient="index")
        raw_data = pd.DataFrame.from_dict(raw_wo_table, orient="index")
        # execution
        renamed = rename_cols(raw_data, COLUMN_MAPPING)
        # validation
        assert sorted(renamed.columns) == sorted(expected.columns)


class TestCastInitTypes:
    """Class for testing the cast_init_types function"""

    def test_cast_init_types_is_function(self):
        """Tests that the cast_init_types function is a function"""
        assert callable(cast_init_types)

    def test_cast_init_types_gets_right_types(self):
        """Tests that the cast_init_types function results in the
        expected data types."""
        # setup
        raw_data = pd.DataFrame.from_dict(raw_wo_table, orient="index")
        renamed = rename_cols(raw_data, COLUMN_MAPPING)
        print(renamed.columns)
        # execution
        type_cast = cast_init_types(renamed)
        # validation
        assert all(  # Check text columns
            is_object_dtype(type_cast[col])
            for col in type_cast[OBJECT_COLS].columns
        )
        assert all(  # Check integer columns
            is_int64_dtype(type_cast[col])
            for col in type_cast[INT_COLS].columns
        )
        assert all(  # Check float columns
            is_float_dtype(type_cast[col])
            for col in type_cast[FLOAT_COLS].columns
        )
        assert all(  # Check date columns
            is_datetime64_dtype(type_cast[col])
            for col in type_cast[DATE_COLS].columns
        )
        assert all(  # Check boolean columns
            is_bool_dtype(type_cast[col])
            for col in type_cast[BOOL_COLS].columns
        )


class TestReplaceValues:
    """Class for testing the replace_values function"""

    def test_cast_init_types_is_function(self):
        """Tests that the cast_init_types function is a function"""
        assert callable(replace_values)

    def test_replace_values_gets_right_result(self):
        """Tests that the replace_values function produces the
        expected results."""
        # setup
        expected = pd.DataFrame.from_dict(
            intermediate_wo_table, orient="index"
        )
        raw_data = pd.DataFrame.from_dict(raw_wo_table, orient="index")
        renamed = rename_cols(raw_data, COLUMN_MAPPING)
        type_cast = cast_init_types(renamed)
        # execution
        replaced = replace_values(type_cast)
        assert replaced[["road_call", "accident"]].equals(
            expected[["road_call", "accident"]]
        )


# def replace_values(df: pd.DataFrame) -> pd.DataFrame:
#     """Replaces values to allow consistent typing.

#     Args:
#         df (pd.DataFrame): Input dataframe

#     Returns:
#         pd.DataFrame: Output dataframe
#     """
#     df = df.copy()
#     mapper = {"Y": 1, "N": 0}
#     df[["is_off_schedule", "is_on_schedule"]] = df[
#         ["is_off_schedule", "is_on_schedule"]
#     ].replace(mapper)
#     return df


# def cast_types(df: pd.DataFrame) -> pd.DataFrame:
#     """After initial type-casting and value replacement, we have
#     a bit more to do to get the adjusted data cast to
#     the right types.

#     Args:
#         df (pd.DataFrame): Input dataframe

#     Returns:
#         pd.DataFrame: Output dataframe
#     """
#     df = df.copy()
#     df[["is_off_schedule", "is_on_schedule"]] = df[
#         ["is_off_schedule", "is_on_schedule"]
#     ].astype(bool)
#     return df


# def prepare_data(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
#     """Runs all data-preparation functions in sequence to
#     complete workflow.

#     Args:
#         df (pd.DataFrame): Input dataframe
#         mapping (dict): Output dataframe

#     Returns:
#         pd.DataFrame: _description_
#     """
#     df = df.copy()
#     df = rename(df, mapping=mapping)
#     df = cast_init_types(df)
#     df = replace_values(df)
#     df = cast_types(df)
#     return df
