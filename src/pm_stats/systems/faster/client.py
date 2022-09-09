# pylint: disable E1101
from __future__ import annotations
from typing import List

import pandas as pd
import sqlalchemy as db
import pyodbc
from sqlalchemy import select
from sqlalchemy.orm import Session, aliased
from sqlalchemy.engine import URL, Row
from dynaconf import Dynaconf

from pm_stats.config import settings

# from pm_stats.systems.faster.models import WorkOrder

Records = List[dict]


class Faster:
    """Handles connection and read/write functions for Faster database."""

    def __init__(
        self, config: Dynaconf = settings, conn_url: str = None
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
        self._work_orders: Records = None

    @property
    def work_orders(self):
        """Returns a list of work orders."""
        if not self._work_orders:
            raise NotImplementedError(
                "The list of work orders hasn't been queried yet. "
                "Use Faster.get_work_orders() to retrieve that list."
            )
        return self._citations

    def _rows_to_dicts(self, cursor):
        """xyz"""
        return [row._asdict() for row in cursor.all()]

    # def get_work_orders(self, limit: int = 100) -> DataBaseRows:
    #     """xyz"""
    #     # create aliases for the tables
    #     cit = aliased(Citation, name="cit")

    #     # extract the columns to include in the query
    #     cit_cols = [getattr(cit, col) for col in cit.columns]

    #     # build the query
    #     query = select(*cit_cols).limit(limit)
    #     with Session(self.engine) as session:
    #         rows = session.execute(query).fetchall()
    #     return DataBaseRows(rows)


class DataBaseRows:
    """A class that provides simplified access to the results of a SQL query"""

    def __init__(self, rows: List[Row], row_type: str = "columns") -> None:
        """Inits the DataBaseRows class"""
        self.rows = rows
        self.row_type = row_type
        self.cols = rows[0]._fields

    @property
    def dataframe(self) -> pd.DataFrame:
        """Returns the rows as a Pandas dataframe"""
        return pd.DataFrame(self.rows, columns=self.cols)

    @property
    def records(self) -> List[dict]:
        """Returns the rows as a list of dictionaries"""
        return [row._asdict() for row in self.rows]


f = Faster()
