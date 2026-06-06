from pydantic import BaseModel
from datetime import datetime

class ScheduleCreate(BaseModel):
    medication_id: int
    recurrence_pattern: str
    reminder_time: datetime 
    timezone: str

class ScheduleResponse(BaseModel):
    id: int
    medication_id: int   
    recurrence_pattern: str 
    reminder_time: datetime
    timezone: str

    class Config:
        from_attributes = True

