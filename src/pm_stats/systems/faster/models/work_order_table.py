# from contextlib import AbstractAsyncContextManager
# from logging.config import _LoggerConfiguration
import pm_stats.systems.faster.models.base as base

WORK_ORDER_COLS = [
    "asset_id",
    "asset_number",
    "organization",
    "out_of_service_date",
    "department",
    "agency",
    "vehicle_year",
    "make",
    "model",
    "vehicle_class",
    "pm_cycle_length",
    "due_month_date",
    "calendar_year",
    "month_number",
    "month_name",
    "pm_due_date",
    "done_at",
    "work_order_date",
    "days_late",
    "days_late_adjusted",
    "leeway",
    "on_time",
    "late",
    "off_schedule",
    "on_schedule",
    "closed_date",
    "days_in_shop",
    "number_of_repairs",
    "total_work_order_cost",
    "labor_hours",
    "sublet_hours",
    "symptom",
    "road_call",
    "accident",
    "work_order_number",
    "preceding_pm_miles",
    "this_pm_miles",
    "miles_driven",
]


class WorkOrder(base.Base):
    "Table that contains information about work orders"
    __tablename__ = "ZZ_Martix_CostPMLate"

    # columns
    asset_id = base.Column("ASSETID", base.Integer, nullable=False)
    asset_number = base.Column("ASSETNUMBER", base.String, nullable=False)
    organization = base.Column("ORGANIZATION", base.String)
    out_of_service_date = base.Column("OUT OF SERVICE DATE", base.DateTime)
    department = base.Column("DEPARTMENT", base.String)
    agency = base.Column("AGENCY", base.String)
    assigned_asset_shop = base.Column("ASSIGNED ASSET SHOP", base.String)
    citation_status = base.Column("CITATIONSTATUS", base.String)
    vehicle_year = base.Column("VEH YEAR", base.Integer)
    make = base.Column("MAKE", base.String)
    vehicle_class = base.Column("CLASS", base.String)
    vehicle_type = base.Column("VEHICLE TYPE", base.String)
    pm_cycle_length = base.Column("PM LENGTH AT THE TIME", base.String)
    due_month_date = base.Column("DUEMONTHDATE", base.DateTime)
    calendar_year = base.Column("CALENDAR YEAR", base.Integer)
    fiscal_year = base.Column("FISCAL YEAR", base.Integer)
    month_number = base.Column("MONTH", base.Integer)
    month_name = base.Column("MONTHNAME", base.String)
    pm_due_date = base.Column("PM DUE DATE", base.DateTime)
    done_at = base.Column("DONE AT", base.DateTime)
    work_order_date = base.Column("WORK ORDER DATE", base.DateTime)
    days_late = base.Column("DAYS LATE NO 10%", base.Float)
    days_late_adjusted = base.Column("DAYS LATE 10%", base.Float)
    leeway = base.Column("LEEWAY", base.Float)
    #on_time = base.Column("ONTIME", base.Integer)
    late = base.Column("LATE", base.Integer)
    off_schedule = base.Column("OFFSCHEDULE", base.Integer)
    on_schedule = base.Column("ONTIME", base.Integer)
    closed_date = base.Column("CLOSED DATE", base.DateTime)
    days_in_shop = base.Column("ONTIME", base.Float)
    number_of_repairs = base.Column("NUMBER OF REPAIRS", base.Integer)
    total_work_order_cost = base.Column("TOTAL WORK ORDER COST", base.Float)
    labor_hours = base.Column("LABOR HOURS", base.Float)
    sublet_hours = base.Column("SUBLET HOURS", base.Float)
    symptom = base.Column("SYMPTOM", base.String)
    road_call = base.Column("ROADCALL", base.String)
    accident = base.Column("ACCIDENT", base.String)
    work_order_number = base.Column("WORK ORDER", base.String)
    preceding_pm_miles = base.Column("PRECEDING PM MILES", base.Integer)
    this_pm_miles = base.Column("THIS PM MILEAGE", base.Integer)
    miles_driven = base.Column("MILES DRIVEN", base.Integer)
    # column list for querying
    columns = WORK_ORDER_COLS
