from pydantic import BaseModel
from datetime import datetime

class NotificationCreate(BaseModel):
    user_id: int
    notification_type: str

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    notification_type: str
    sent_at: datetime

    class Config:
        from_attributes = True
    