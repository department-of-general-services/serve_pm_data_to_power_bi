from pm_stats.systems.faster import Faster, QUERY
from pm_stats.utils import (
    aggregate_wos_to_assets,
    compute_vehicle_age,
    prepare_data,
    AGG_MAPPING,
    VEHICLE_ATTRIBUTES,
)
from pm_stats.analysis import MultipleRegression
from pm_stats.systems.faster import COLUMN_MAPPING

if __name__ == "__main__":
    # obtain the data by querying stored procedure
    f = Faster(asset_profile="caprice_3_month_cycle")
    work_orders_raw = f.get_work_orders(query=QUERY)
    work_orders = prepare_data(work_orders_raw, COLUMN_MAPPING)
    print(f"Length of work orders dataset: {len(work_orders)}")
    # perform aggregation
    assets = aggregate_wos_to_assets(
        work_orders, AGG_MAPPING, VEHICLE_ATTRIBUTES
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
