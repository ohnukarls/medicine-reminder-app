from pydantic import BaseModel
from datetime import datetime

class ReminderCreate(BaseModel):
    schedule_id: int
    
class ReminderResponse (BaseModel):
    id: int
    schedule_id: int
    sent_at: datetime
    status: str
    time: datetime
    frequency: str
    days_of_week: str
    is_active: bool
    start_date: datetime
    end_date: datetime
    last_sent_at: datetime

    class Config:
        from_attributes = True
    