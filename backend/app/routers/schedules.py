from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.redis import redis_client
import json

from app.database import get_db
from app.models.schedules import Schedule
from app.models.users import User
from app.schemas.schedules import (
    ScheduleCreate,
    ScheduleResponse
)
from app.core.dependencies import get_current_user

CACHE_TTL_SECONDS = 300  # Cache time-to-live in seconds

router = APIRouter(
    prefix="/schedules",        
    tags=["Schedules"]
) 

def get_schedules_cache_key(user_id: int) -> str:
    return f"user:{user_id}:schedules"


@router.get("/", response_model=list[ScheduleResponse])
def read_schedules(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cache_key = get_schedules_cache_key(current_user.id)

    cached = redis_client.get(cache_key)

    if cached:
        return json.loads(cached)

    schedules = db.query(Schedule).filter(Schedule.user_id == current_user.id).all()

    schedule_data = [
        ScheduleResponse.model_validate(schedule).model_dump()
        for schedule in schedules
    ]

    redis_client.setex(
        cache_key,
        CACHE_TTL_SECONDS,
        json.dumps(schedule_data)
    )

    return schedule_data

@router.post("/", response_model=ScheduleResponse)
def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cache_key = get_schedules_cache_key(current_user.id)
    new_schedule = Schedule(
        user_id=current_user.id,
        medication_id=schedule.medication_id,
        recurrence_pattern=schedule.recurrence_pattern,
        reminder_time=schedule.reminder_time,
        timezone=schedule.timezone,
    )
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    redis_client.delete(cache_key)
    return new_schedule

@router.put("/{schedule_id}", response_model=ScheduleResponse)
def update_schedule(schedule_id: int, schedule_update: ScheduleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cache_key = get_schedules_cache_key(current_user.id)
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id, Schedule.user_id == current_user.id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    schedule.medication_id = schedule_update.medication_id
    schedule.recurrence_pattern = schedule_update.recurrence_pattern
    schedule.reminder_time = schedule_update.reminder_time
    schedule.timezone = schedule_update.timezone

    db.commit()
    db.refresh(schedule)
    redis_client.delete(cache_key)
    return schedule

@router.delete("/{schedule_id}", status_code=204)
def delete_schedule(schedule_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cache_key = get_schedules_cache_key(current_user.id)
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id, Schedule.user_id == current_user.id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    db.delete(schedule)
    db.commit()
    redis_client.delete(cache_key)