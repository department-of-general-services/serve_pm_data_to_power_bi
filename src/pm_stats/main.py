from pathlib import Path
from pm_stats.systems.faster import Faster
from pm_stats.analysis import MultipleRegression
from pm_stats.utils.utility import load_experiments

if __name__ == "__main__":
    experiments_path = Path.cwd() / "src" / "pm_stats" / "experiments.yaml"
    experiment = load_experiments(experiments_path)
    # initiate an object of class Faster, with an asset profile
    f = Faster(
        asset_profile="ford_F250_HP_4_month_cycle",
        experiment=experiment,
    )
    print(f"Length of work orders dataset: {len(f.work_orders)}")
    # obtain data aggregated to asset level
    assets = f.assets_in_scope
    print(
        assets[
            [
                "starting_mileage",
                "weeks_late_mean",
                "vehicle_years_in_service",
                "total_cost",
            ]
        ].head()
    )
    # drop vehicles with only one work order
    cond_multiple_wos = (
        assets["work_order_count"] >= experiment["minimum_work_orders"]
    )
    assets = assets[cond_multiple_wos]
    cond_not_brand_new = (
        assets["vehicle_years_in_service"] >= experiment["minimum_years_in_service"]
    )
    assets = assets[cond_multiple_wos]

    print(f"Length of assets dataset: {len(assets)}")
    print(assets.columns)
    # define x and y matrix
    mr = MultipleRegression(
        data=assets,
        x_cols=[
            # "total_miles_driven",
            "miles_driven_mean",
            "weeks_late_mean",
            "starting_mileage",
            # "vehicle_years_in_service",
        ],
        y_col=experiment["dependent_variable"],
    )
    # report on correlations
