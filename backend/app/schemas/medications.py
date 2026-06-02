from pydantic import BaseModel
class MedicationCreate(BaseModel):
    user_id: int 
    medication_name: str
    dosage: str
    instructions: str | None = None

class MedicationResponse(BaseModel):
    id: int
    user_id: int
    medication_name: str
    dosage: str
    instructions: str | None = None

    class Config: 
        from_attributes = True