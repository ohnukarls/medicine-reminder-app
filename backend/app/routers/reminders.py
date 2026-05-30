from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.reminders import Reminder
from app.models.users import User
from app.schemas.reminders import (
    ReminderCreate,
    ReminderResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/reminders",    
    tags=["reminders"]
)

@router.get("/", response_model=list[ReminderResponse])
def read_reminders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    reminders = db.query(Reminder).filter(Reminder.user_id == current_user.id).all()
    return reminders


@router.post("/", response_model=ReminderResponse)
def create_reminder(reminder: ReminderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_reminder = Reminder(
        medication_id=reminder.medication_id,
        time=reminder.time,
        user_id=current_user.id
    )
    db.add(new_reminder)
    db.commit()
    db.refresh(new_reminder)
    return new_reminder

@router.delete("/{reminder_id}", status_code=204)
def delete_reminder(reminder_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id, Reminder.user_id == current_user.id).first()
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    db.delete(reminder)
    db.commit()

