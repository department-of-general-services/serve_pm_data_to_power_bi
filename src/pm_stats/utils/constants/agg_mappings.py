# set aggregation
AGG_MAPPING = {
    "work_order_number": ["nunique"],
    "done_at_date": ["min", "max"],
    "current_pm_mileage": ["min", "max"],
    "days_late": ["mean", "median"],
    "miles_driven": ["mean"],
    "work_order_total_cost": ["sum"],
}
# Renaming scheme for aggregated work-order data
AGG_RENAMING = {
    "work_order_number_nunique": "work_order_count",
    "done_at_date_min": "first_completion_date",
    "done_at_date_max": "last_completion_date",
    "current_pm_mileage_min": "starting_mileage",
    "current_pm_mileage_max": "ending_mileage",
    "days_late_mean": "days_late_mean",
    "days_late_median": "days_late_median",
    "miles_driven_mean": "miles_driven_mean",
    "work_order_total_cost_sum": "total_cost",
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
