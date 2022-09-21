# pylint: disable=E1101, C0103
from __future__ import annotations
from typing import List

import pandas as pd
import sqlalchemy as db
import pyodbc
from sqlalchemy.engine import URL
from dynaconf import Dynaconf

from pm_stats.config import settings
from pm_stats.systems.faster.models import (
    ASSETS_QUERY,
    WORK_ORDERS_QUERY,
    PARAMS,
    COLUMN_MAPPING,
)
from pm_stats.utils import prepare_data
from pm_stats.utils.constants import AGG_MAPPING, VEHICLE_ATTRIBUTES
from pm_stats.utils.aggregations import aggregate_and_merge
from pm_stats.utils.feature_engineering import engineer_features

Records = List[dict]


class Faster:
    """Handles connection and read/write functions for Faster database."""

    def __init__(
        self,
        asset_profile: str,
        config: Dynaconf = settings,
        conn_url: str = None,
        testing_data: pd.DataFrame = None,
    ) -> None:
        """Creates engine object."""
        if isinstance(testing_data, pd.DataFrame):
            self.work_orders = testing_data
            # needs testing version of asset_details
        else:
            if not conn_url:
                conn_str = (
                    "Driver={SQL Server};"
                    f"Server={config.faster_server};"
                    f"Database={config.faster_database};"
                    f"Trusted_Connection=yes;"
                )
                pyodbc.pool = False
                conn_url = URL.create(
                    "mssql+pyodbc", query={"odbc_connect": conn_str}
                )
            self.engine = db.create_engine(conn_url, pool_pre_ping=True)
            self.asset_profile: str = asset_profile
            self.work_orders: pd.DataFrame = self.get_work_orders(
                query=WORK_ORDERS_QUERY
            )
            self.work_orders = prepare_data(self.work_orders, COLUMN_MAPPING)
            self.asset_details: pd.DataFrame = self.get_asset_details(
                query=ASSETS_QUERY
            )
            self.assets_in_scope = aggregate_and_merge(
                self.work_orders,
                self.asset_details,
                AGG_MAPPING,
                VEHICLE_ATTRIBUTES,
            )
            self.assets_in_scope = engineer_features(self.assets_in_scope)

    def return_work_orders(self):
        """Returns a list of work orders."""
        if not self.work_orders:
            raise NotImplementedError(
                "The list of work orders hasn't been queried yet. "
                "Use Faster.get_work_orders() to retrieve that list."
            )
        return self.work_orders

    def get_work_orders(self, query: str) -> pd.DataFrame:
        """xyz"""
        print("Getting work orders")
        params = PARAMS[self.asset_profile]
        df = pd.read_sql_query(db.text(query), self.engine, params=params)
        return df

    def get_asset_details(self, query: str) -> pd.DataFrame:
        """xyz"""
        print("Getting asset details.")
        df = pd.read_sql_query(db.text(query), self.engine)
        return df
