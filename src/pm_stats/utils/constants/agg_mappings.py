# set aggregation
AGG_MAPPING = {
    "current_pm_mileage": ["min", "max"],
    "days_late": ["mean"],
    "miles_driven": ["mean"],
    "pm_due_date": ["nunique"],
    "work_order_total_cost": ["sum"],
}
VEHICLE_ATTRIBUTES = [
    "asset_number",
    "asset_id",
    "vehicle_year",
    "department",
    "make",
    "model",
    "pm_cycle_length",
]
