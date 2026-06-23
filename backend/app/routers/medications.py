from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.medications import Medication
from app.models.users import User
from app.schemas.medications import (
    MedicationCreate,
    MedicationResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/medications",   
    tags=["Medications"]
)
@router.get("/", response_model=list[MedicationResponse])
def read_medications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    medications = db.query(Medication).filter(Medication.user_id == current_user.id).all()
    return medications

@router.post("/", response_model=MedicationResponse)
def create_medication(medication: MedicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_medication = Medication(
        user_id=current_user.id,
        medication_name=medication.medication_name,
        dosage=medication.dosage,
        instructions=medication.instructions
    )
    db.add(new_medication)
    db.commit()
    db.refresh(new_medication)
    return new_medication

@router.put("/{medication_id}", response_model=MedicationResponse)
def update_medication(medication_id: int, medication_update: MedicationCreate, db:  Session = Depends(get_db), current_user: User = Depends(get_current_user)):     
    medication = db.query(Medication).filter(Medication.id == medication_id, Medication.user_id == current_user.id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    medication.medication_name = medication_update.medication_name
    medication.dosage = medication_update.dosage
    medication.instructions = medication_update.instructions
    db.commit()
    db.refresh(medication)
    return medication

@router.delete("/{medication_id}", status_code=204)
def delete_medication(medication_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    medication = db.query(Medication).filter(Medication.id == medication_id, Medication.user_id == current_user.id).first()
    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(medication)
    db.commit()