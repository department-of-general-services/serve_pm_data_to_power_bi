from pathlib import Path
import pandas as pd

from pm_stats.systems.faster import Faster
from pm_stats.analysis import MultipleRegression
from pm_stats.utils.utility import load_experiments
from pm_stats.systems.faster.models import PARAMS

if __name__ == "__main__":
    experiments_path = Path.cwd() / "src" / "pm_stats" / "experiments.yaml"
    experiment = load_experiments(experiments_path)
    # initiate an object of class Faster, with an asset profile
    f = Faster()
    assets_output = pd.DataFrame()
    for asset_profile in PARAMS:
        f.query(asset_profile=f"{asset_profile}", experiment=experiment)
        # obtain data aggregated to asset level
        assets = f.assets_in_scope
        # drop vehicles with too few work orders
        cond_multiple_wos = assets["work_order_count"] >= int(
            experiment["minimum_work_orders"]
        )
        assets = assets[cond_multiple_wos]
        cond_not_brand_new = (
            assets["vehicle_years_in_service"]
            >= experiment["minimum_years_in_service"]
        )
        assets = assets[cond_multiple_wos]
        print(f"ASSET PROFILE: {asset_profile}")
        print(f"Number of Observations: {len(assets)}")
        # define x and y matrix
        mr = MultipleRegression(
            data=assets,
            x_cols=experiment["predictors"],
            y_col=experiment["dependent_variable"],
        )
        # report on correlations
