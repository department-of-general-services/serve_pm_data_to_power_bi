# from contextlib import AbstractAsyncContextManager
# from logging.config import _LoggerConfiguration

QUERY = """
    SET NOCOUNT ON;
    SET ARITHABORT ON;
    EXEC [Baltimore].[ZZ_Martix_CostPMLate]
    @StartDate = :start_date,
    @EndDate = :end_date,
    @TimeZone = :time_zone,
    @Length = :length,
    @Modelid = :model_id,
    @Usage = :usage;
    """

PARAMS = {
    "caprice_3_month_cycle": {
        "start_date": "20190701",
        "end_date": "20220901",
        "time_zone": 3,
        "length": 3,
        "model_id": 842,
        "usage": "MP",
    },
    "caprice_1_month_cycle": {
        "start_date": "20190701",
        "end_date": "20220901",
        "time_zone": 3,
        "length": 1,
        "model_id": 842,
        "usage": "MP",
    },
}

COLUMN_MAPPING = {
    "AssetNumber": "asset_number",
    "Organization": "organization",
    "Out of Service Date": "out_of_service_date",
    "Department": "department",
    "Agency": "agency",
    "Assigned Asset Shop": "assigned_asset_shop",
    "Veh Year": "vehicle_year",
    "Make": "make",
    "Model": "model",
    "Class": "class",
    "Vehicle Type": "vehicle_type",
    "Pm Length at the time": "pm_cycle_length",
    "DueMonthDate": "due_month_date",
    "Calendar Year": "calendar_year",
    "Fiscal Year": "fiscal_year",
    "Month": "month_number",
    "MonthName": "month_name",
    "PM Due Date": "pm_due_date",
    "Done At": "done_at_date",
    "Work Order Date": "work_order_date",
    "Days Late No10%": "days_late",
    "Days Late 10%": "days_late_adjusted",
    "Leeway": "leeway",
    "OnTime": "is_ontime",
    "Late": "is_late",
    "OffSchedule": "is_off_schedule",
    "OnSchedule": "is_on_schedule",
    "Closed Date": "closed_date",
    "Days In Shop": "days_in_shop",
    "Number of Repairs": "number_of_repairs",
    "Total Work Order Cost": "work_order_total_cost",
    "Labor hours": "labor_hours",
    "Sublet Hours": "sublet_hours",
    "Symptom": "symptom",
    "RoadCall": "road_call",
    "Accident": "accident",
    "Work Order": "work_order_number",
    "Preceding PM Miles": "preceding_pm_mileage",
    "This PM Mileage": "current_pm_mileage",
    "Miles Driven": "miles_driven",
}

OBJECT_COLS = [
    "accident",
    "agency",
    "asset_number",
    "assigned_asset_shop",
    "class",
    "department",
    "is_off_schedule",
    "is_on_schedule",
    "make",
    "model",
    "organization",
    "pm_cycle_length",
    "road_call",
    "symptom",
    "vehicle_type",
    "work_order_number",
]
INT_COLS = [
    "calendar_year",
    "fiscal_year",
    "month_number",
    "number_of_repairs",
    "vehicle_year",
]
DATE_COLS = [
    "closed_date",
    "due_month_date",
    "pm_due_date",
    "done_at_date",
    "work_order_date",
]
FLOAT_COLS = [
    "current_pm_mileage",
    "days_in_shop",
    "days_late",
    "days_late_adjusted",
    "labor_hours",
    "leeway",
    "miles_driven",
    "preceding_pm_mileage",
    "sublet_hours",
    "work_order_total_cost",
]
BOOL_COLS = ["is_ontime", "is_late"]
