from datetime import datetime, timedelta
from pydantic import BaseModel, validator

class TimeRangeParams(BaseModel):
    start_time: datetime
    end_time: datetime
    @validator('end_time')
    def validate_time_range(cls,end_time,values):
        start_time = values.get('start_time')
        if start_time is None:
            return end_time
        if end_time - start_time > timedelta(days=2):
            raise ValueError("Time range must be less than 2 days")
        if start_time > end_time:
            raise ValueError("Start time must be before end time")
        return end_time