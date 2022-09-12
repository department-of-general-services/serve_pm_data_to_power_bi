from pm_stats.systems.faster import Faster, QUERY
from pm_stats.utils.utils import prepare_data
from pm_stats.analysis import MultipleRegression

if __name__ == "__main__":
    # obtain the data by querying stored procedure
    f = Faster()
    work_orders_raw = f.get_work_orders(query=QUERY)
    work_orders = prepare_data(work_orders_raw)
    # take the average
    averages = (
        work_orders.groupby(by="asset_number")[
            ["days_late", "miles_driven", "work_order_total_cost"]
        ]
        .mean()
        .dropna()
    )
    print(averages.info())
    # define x and y matrix
    mr = MultipleRegression(
        data=work_orders,
        x_cols=["days_late", "miles_driven"],
        y_col="labor_hours",
    )
    # report on correlations
