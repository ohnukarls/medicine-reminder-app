from pydantic import BaseModel
from datetime import datetime

class NotificationLogCreate(BaseModel):
    schedule_id: int
    status: str
    message: str | None = None

class NotificationLogResponse(BaseModel):
    id: int
    schedule_id: int
    status: str
    message: str | None = None
    sent_at: datetime 

    class Config:
        from_attributes = True
    