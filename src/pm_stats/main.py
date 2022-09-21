from pm_stats.systems.faster import Faster, WORK_ORDERS_QUERY
from pm_stats.utils import (
    aggregate_wos_to_assets,
    compute_vehicle_age,
    prepare_data,
    AGG_MAPPING,
    VEHICLE_ATTRIBUTES,
)
from pm_stats.analysis import MultipleRegression

if __name__ == "__main__":
    # initiate an object of class Faster, with an asset profile
    f = Faster(asset_profile="caprice_3_month_cycle")
    f.get_work_orders(query=WORK_ORDERS_QUERY)
    print(f"Length of work orders dataset: {len(f.work_orders)}")
    # perform aggregation
    assets = aggregate_wos_to_assets(
        f.work_orders, AGG_MAPPING, VEHICLE_ATTRIBUTES
    )
    # drop vehicles with only one work order
    cond_multiple_wos = assets["pm_due_date_nunique"] > 1
    assets = assets[cond_multiple_wos]
    # perform feature engineering
    assets = compute_vehicle_age(assets)
    print(f"Length of assets dataset: {len(assets)}")
    # define x and y matrix
    mr = MultipleRegression(
        data=assets,
        x_cols=[
            "current_pm_mileage_min",
            "days_late_mean",
        ],
        y_col="work_order_total_cost_sum",
    )
    # report on correlations
