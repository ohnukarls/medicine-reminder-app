from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.redis import redis_client
import json

from app.database import get_db
from app.models.medications import Medication
from app.models.users import User
from app.schemas.medications import (
    MedicationCreate,
    MedicationResponse
)
from app.core.dependencies import get_current_user

CACHE_TTL_SECONDS = 300  # Cache time-to-live in seconds

router = APIRouter(
    prefix="/medications",   
    tags=["Medications"]
)

def get_medications_cache_key(user_id: int) -> str:
    return f"user:{user_id}:medications"


@router.get("/", response_model=list[MedicationResponse])
def read_medications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cache_key = get_medications_cache_key(current_user.id)
    cached = redis_client.get(cache_key)
    
    if cached:
        return json.loads(cached)

    medications = db.query(Medication).filter(Medication.user_id == current_user.id).all()

    medication_data = [   
        MedicationResponse.model_validate(medication).model_dump()
        for medication in medications
    ]

    redis_client.setex(
        cache_key,
        CACHE_TTL_SECONDS,
        json.dumps(medication_data)
    )

    return medication_data

@router.post("/", response_model=MedicationResponse)
def create_medication(medication: MedicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cache_key = get_medications_cache_key(current_user.id)
    new_medication = Medication(
        user_id=current_user.id,
        medication_name=medication.medication_name,
        dosage=medication.dosage,
        instructions=medication.instructions
    )
    db.add(new_medication)
    db.commit()
    redis_client.delete(cache_key)
    db.refresh(new_medication)
    return new_medication

@router.put("/{medication_id}", response_model=MedicationResponse)
def update_medication(medication_id: int, medication_update: MedicationCreate, db:  Session = Depends(get_db), current_user: User = Depends(get_current_user)):     
    cache_key = get_medications_cache_key(current_user.id)
    medication = db.query(Medication).filter(Medication.id == medication_id, Medication.user_id == current_user.id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    medication.medication_name = medication_update.medication_name
    medication.dosage = medication_update.dosage
    medication.instructions = medication_update.instructions
    db.commit()
    redis_client.delete(cache_key)
    db.refresh(medication)
    return medication

@router.delete("/{medication_id}", status_code=204)
def delete_medication(medication_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cache_key = get_medications_cache_key(current_user.id)
    medication = db.query(Medication).filter(Medication.id == medication_id, Medication.user_id == current_user.id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(medication)
    db.commit()
    redis_client.delete(cache_key)