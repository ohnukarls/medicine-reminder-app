```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.reminders import Reminder
from app.models.schedules import Schedule
from app.models.users import User
from app.schemas.reminders import (
    ReminderResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/reminders",
    tags=["reminders"]
)


@router.get("/", response_model=list[ReminderResponse])
def read_reminders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    reminders = (
        db.query(Reminder)
        .join(Schedule)
        .filter(Schedule.user_id == current_user.id)
        .all()
    )

    return reminders


@router.get("/{reminder_id}", response_model=ReminderResponse)
def read_reminder(
    reminder_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    reminder = (
        db.query(Reminder)
        .join(Schedule)
        .filter(
            Reminder.id == reminder_id,
            Schedule.user_id == current_user.id
        )
        .first()
    )

    if not reminder:
        raise HTTPException(
            status_code=404,
            detail="Reminder not found"
        )

    return reminder


@router.delete("/{reminder_id}", status_code=204)
def delete_reminder(
    reminder_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    reminder = (
        db.query(Reminder)
        .join(Schedule)
        .filter(
            Reminder.id == reminder_id,
            Schedule.user_id == current_user.id
        )
        .first()
    )

    if not reminder:
        raise HTTPException(
            status_code=404,
            detail="Reminder not found"
        )

    db.delete(reminder)
    db.commit()

    return
