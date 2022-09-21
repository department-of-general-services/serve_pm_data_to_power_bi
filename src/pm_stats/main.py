from pm_stats.systems.faster import Faster
from pm_stats.analysis import MultipleRegression

if __name__ == "__main__":
    # initiate an object of class Faster, with an asset profile
    f = Faster(asset_profile="interceptor_utility_1_month_cycle")
    print(f"Length of work orders dataset: {len(f.work_orders)}")
    print(f"COLUMNS: {f.work_orders.columns}")
    # obtain data aggregated to asset level
    assets = f.assets_in_scope
    # drop vehicles with only one work order
    cond_multiple_wos = assets["pm_due_date_nunique"] > 1
    assets = assets[cond_multiple_wos]

    print(f"Length of assets dataset: {len(assets)}")
    print(assets.info())
    # define x and y matrix
    mr = MultipleRegression(
        data=assets,
        x_cols=[
            # "current_pm_mileage_min",
            "days_late_mean",
            "vehicle_days_in_service",
        ],
        y_col="work_order_total_cost_sum",
    )
    # report on correlations
