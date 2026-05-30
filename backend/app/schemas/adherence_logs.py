from pydantic import BaseModel

class AdherenceLogCreate(BaseModel):
    medication_id: int
    taken: bool

class AdherenceLogResponse(BaseModel):
    id: int
    user_id: int
    medication_id: int
    taken_at: datetime
    status: str

    class Config:
        from_attributes = True