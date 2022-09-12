# from contextlib import AbstractAsyncContextManager
# from logging.config import _LoggerConfiguration
import pm_stats.systems.faster.models.base as base

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
    "caprice": {
        "start_date": "20210701",
        "end_date": "20220901",
        "time_zone": 3,
        "length": 3,
        "model_id": 842,
        "usage": "MP",
    }
}
