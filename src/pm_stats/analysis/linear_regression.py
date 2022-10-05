# pylint: disable=C0103
from typing import List
import pandas as pd
import statsmodels.api as sm


class MultipleRegression:
    """Class that stores the model."""

    def __init__(
        self,
        data: pd.DataFrame,
        x_cols: List[str],
        y_col: str,
    ) -> None:
        self.data = data
        self.X = data[x_cols]
        self.y = data[y_col]
        self.model = self.fit_model()

    @property
    def number_of_predictors(self) -> int:
        """Returns the number of predictor columns"""
        return len(self.X.columns)

    def fit_model(self) -> str:
        """Fits a multiple linear regression model to the data."""
        self.X = sm.add_constant(self.X)
        estimate = sm.OLS(self.y, self.X).fit()
        rsquared = round(estimate.rsquared, 2)
        adj_rsquared = round(estimate.rsquared_adj, 2)
        print(f"Rsquared: {rsquared}\nAdjusted Rsquared: {adj_rsquared}")
        print("\n")
        print(estimate.params)
        print("\n")
        print(estimate.pvalues)
        print("\n\n")
        return estimate
