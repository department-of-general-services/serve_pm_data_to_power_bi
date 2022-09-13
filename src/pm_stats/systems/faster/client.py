# pylint: disable=E1101, C0103
from __future__ import annotations
from typing import List

import pandas as pd
import sqlalchemy as db
import pyodbc
from sqlalchemy.engine import URL
from dynaconf import Dynaconf

from pm_stats.config import settings
from pm_stats.systems.faster.models import PARAMS, QUERY

Records = List[dict]


class Faster:
    """Handles connection and read/write functions for Faster database."""

    def __init__(
        self,
        config: Dynaconf = settings,
        conn_url: str = None,
        vehicle_model: str = "caprice",
    ) -> None:
        """Creates engine object."""
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
        self.vehicle_model = vehicle_model
        self._work_orders: pd.DataFrame = None

    @property
    def work_orders(self):
        """Returns a list of work orders."""
        if not self._work_orders:
            raise NotImplementedError(
                "The list of work orders hasn't been queried yet. "
                "Use Faster.get_work_orders() to retrieve that list."
            )
        return self._work_orders

    def get_work_orders(self, query: str) -> pd.DataFrame:
        """xyz"""
        print("Getting work orders")
        params = PARAMS[self.vehicle_model]
        df = pd.read_sql_query(db.text(query), self.engine, params=params)
        return df


if __name__ == "__main__":
    f = Faster()
    work_orders = f.get_work_orders(query=QUERY)
