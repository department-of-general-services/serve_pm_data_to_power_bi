# set aggregation
AGG_MAPPING = {
    "work_order_number": ["nunique"],
    "done_at_date": ["min", "max"],
    "current_pm_mileage": ["min", "max"],
    "weeks_late": ["mean", "median"],
    "miles_driven": ["sum", "mean"],
    "labor_hours": ["sum", "mean", "median"],
    "work_order_total_cost": ["sum", "mean", "median"],
}
# Renaming scheme for aggregated work-order data
AGG_RENAMING = {
    "acquire_date": "acquire_date",
    "work_order_number_nunique": "work_order_count",
    "done_at_date_min": "first_completion_date",
    "done_at_date_max": "last_completion_date",
    "current_pm_mileage_min": "starting_mileage",
    "current_pm_mileage_max": "ending_mileage",
    "weeks_late_mean": "weeks_late_mean",
    "weeks_late_median": "weeks_late_median",
    "miles_driven_sum": "total_miles_driven",
    "miles_driven_mean": "miles_driven_mean",
    "labor_hours_sum": "total_labor_hours",
    "labor_hours_mean": "mean_labor_hours",
    "labor_hours_median": "median_labor_hours",
    "work_order_total_cost_sum": "total_cost",
    "work_order_total_cost_mean": "mean_cost",
    "work_order_total_cost_median": "median_cost",
}
# Attributes of the asset that don't vary by work order
VEHICLE_ATTRIBUTES = [
    "asset_number",
    "asset_id",
    "vehicle_year",
    "department",
    "make",
    "model",
    "pm_cycle_length",
]
# Names of the columns that describe mileage and should be divided by 1000
MILEAGE_COLS = [
    "starting_mileage",
    "total_miles_driven",
    "miles_driven_mean",
]
