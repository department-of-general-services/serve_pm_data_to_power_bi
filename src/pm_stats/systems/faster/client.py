# pylint: disable=E1101, C0103
from __future__ import annotations
from typing import List, Optional

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
from pm_stats.utils.assets_feature_engineering import engineer_asset_features

Records = List[dict]


class Faster:
    """Handles connection and read/write functions for Faster database."""

    def __init__(
        self,
        config: Dynaconf = settings,
        testing_data: pd.DataFrame = None,
    ) -> None:
        """Creates engine object."""
        self.work_orders: Optional[pd.DataFrame] = None
        self.asset_details: Optional[pd.DataFrame] = None
        self.assets_in_scope: Optional[pd.DataFrame] = None

        if isinstance(testing_data, pd.DataFrame):
            self.work_orders = testing_data
            # needs testing version of asset_details
        else:
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

    def query(self, asset_profile: str, experiment: dict):
        """Initiates queries to the Faster database.

        Args:
            asset_profile (str): The name of the asset profile definition
            experiment (dict): The configuration of an experiment
        """

        self.get_work_orders(
            asset_profile, experiment=experiment, query=WORK_ORDERS_QUERY
        )
        self.work_orders = prepare_data(self.work_orders, COLUMN_MAPPING)
        self.get_asset_details()
        self.assets_in_scope = aggregate_and_merge(
            self.work_orders,
            self.asset_details,
            AGG_MAPPING,
            VEHICLE_ATTRIBUTES,
        )
        self.assets_in_scope = engineer_asset_features(self.assets_in_scope)

    def get_asset_details(self):
        """Queries the Faster database for background information on all assets.
        This should happen only once.
        """
        if not isinstance(self.asset_details, pd.DataFrame):
            self.asset_details = pd.read_sql_query(
                db.text(ASSETS_QUERY), self.engine
            )

    def return_work_orders(self):
        """Returns a list of work orders."""
        if not self.work_orders:
            raise NotImplementedError(
                "The list of work orders hasn't been queried yet. "
                "Use Faster.get_work_orders() to retrieve that list."
            )
        return self.work_orders

    def get_work_orders(
        self, asset_profile: str, experiment: dict, query: str
    ) -> pd.DataFrame:
        """xyz"""
        print("Getting work orders")
        params = PARAMS[asset_profile]
        params["start_date"] = experiment["start_date"]
        params["end_date"] = experiment["end_date"]
        params["time_zone"] = experiment["time_zone"]
        self.work_orders = pd.read_sql_query(
            db.text(query), self.engine, params=params
        )
