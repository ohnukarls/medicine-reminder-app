from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.schedules import Schedule
from app.models.users import User
from app.schemas.schedules import (
    ScheduleCreate,
    ScheduleResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/schedules",        
    tags=["Schedules"]
) 

@router.get("/", response_model=list[ScheduleResponse])
def read_schedules(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    schedules = db.query(Schedule).filter(Schedule.user_id == current_user.id).all()
    return schedules

@router.post("/", response_model=ScheduleResponse)
def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_schedule = Schedule(
        user_id=current_user.id,
        medication_id=schedule.medication_id,
        recurrence_pattern=schedule.recurrence_pattern,
        reminder_time=schedule.reminder_time, 
        timezone=schedule.timezone
    )
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule

@router.put("/{schedule_id}", response_model=ScheduleResponse)
def update_schedule(schedule_id: int, schedule_update: ScheduleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id, Schedule.user_id == current_user.id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    schedule.medication_id = schedule_update.medication_id
    schedule.recurrence_pattern = schedule_update.recurrence_pattern
    schedule.reminder_time = schedule_update.reminder_time
    schedule.timezone = schedule_update.timezone

    db.commit()
    db.refresh(schedule)
    return schedule

@router.delete("/{schedule_id}", status_code=204)
def delete_schedule(schedule_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id, Schedule.user_id == current_user.id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    db.delete(schedule)
    db.commit()