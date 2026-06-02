from pydantic import BaseModel
from datetime import datetime

class AdherenceLogCreate(BaseModel):
    user_id: int
    medication_id: int
    taken_at: datetime
    status: str  # e.g., "taken", "missed", "late"

class AdherenceLogResponse(BaseModel): 
    id: int
    user_id: int
    medication_id: int
    taken_at: datetime
    status: str 

    class Config:
        from_attributes = True