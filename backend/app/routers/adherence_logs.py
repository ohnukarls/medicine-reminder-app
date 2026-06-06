from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.adherence_logs import Adherence_Log
from app.models.users import User
from app.schemas.adherence_logs import (
    AdherenceLogCreate,
    AdherenceLogResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/adherence_logs",   
    tags=["Adherence_Logs"]
)   

@router.get("/", response_model=list[AdherenceLogResponse]) 
def read_adherence_logs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    logs = db.query(Adherence_Log).filter(Adherence_Log.user_id == current_user.id).all()
    return logs

@router.post("/", response_model=AdherenceLogResponse)
def create_adherence_log(log: AdherenceLogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_log = Adherence_Log(
        user_id=current_user.id,
        medication_id=log.medication_id,
        taken_at=log.taken_at,
        status=log.status     
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

@router.put("/{log_id}", response_model=AdherenceLogResponse)
def update_adherence_log(log_id: int, log_update: AdherenceLogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    log = db.query(Adherence_Log).filter(Adherence_Log.id == log_id, Adherence_Log.user_id == current_user.id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Adherence log not found")
    log.medication_id = log_update.medication_id
    log.taken_at = log_update.taken_at
    log.status = log_update.status
    db.commit()
    db.refresh(log)
    return log
 
@router.delete("/{log_id}", status_code=204)
def delete_adherence_log(log_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    log = db.query(Adherence_Log).filter(Adherence_Log.id == log_id, Adherence_Log.user_id == current_user.id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Adherence log not found")
    db.delete(log)
    db.commit()
