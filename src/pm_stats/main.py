from pm_stats.systems.faster import Faster, QUERY
from pm_stats.utils.utils import prepare_data
from pm_stats.analysis import MultipleRegression
from pm_stats.systems.faster import COLUMN_MAPPING

if __name__ == "__main__":
    # obtain the data by querying stored procedure
    f = Faster()
    work_orders_raw = f.get_work_orders(query=QUERY)
    work_orders = prepare_data(work_orders_raw, COLUMN_MAPPING)
    # set aggregation
    agg_functions = {
        "current_pm_mileage": ["min"],
        "days_late": ["mean"],
        "miles_driven": ["mean"],
        "pm_due_date": ["nunique"],
        "work_order_total_cost": ["sum"],
    }
    # take the average
    vehicles = work_orders.groupby(by="asset_number")[
        [
            "pm_due_date",
            "days_late",
            "miles_driven",
            "current_pm_mileage",
            "work_order_total_cost",
        ]
    ].agg(agg_functions)
    vehicles.columns = vehicles.columns.map("_".join)
    # print(averages.head())
    # print(averages.columns)
    # drop vehicles with only one work order
    cond_multiple_wos = vehicles["pm_due_date_nunique"] > 1
    vehicles = vehicles[cond_multiple_wos]
    # define x and y matrix
    mr = MultipleRegression(
        data=vehicles,
        x_cols=[
            # "current_pm_mileage_min",
            "days_late_mean",
            "miles_driven_mean",
        ],
        y_col="work_order_total_cost_sum",
    )
    # report on correlations
