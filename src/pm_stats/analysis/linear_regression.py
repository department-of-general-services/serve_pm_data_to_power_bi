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
        self.model = self.model()

    @property
    def number_of_predictors(self) -> int:
        """Returns the number of predictor columns"""
        return len(self.X.columns)

    def model(self) -> str:
        """X"""
        self.X = sm.add_constant(self.X)
        estimate = sm.OLS(self.y, self.X).fit()
        print(estimate.summary())