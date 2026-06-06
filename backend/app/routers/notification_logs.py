from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.notification_logs import Notification_Log
from app.models.schedules import Schedule
from app.models.users import User
from app.schemas.notification_logs import (
    NotificationLogCreate,
    NotificationLogResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/notification_logs",        
    tags=["Notification_Logs"]
)

@router.post("/", response_model=NotificationLogResponse)
def create_notification_log(notification: NotificationLogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    schedule = (
    db.query(Schedule)
    .filter(
        Schedule.id == notification.schedule_id,
        Schedule.user_id == current_user.id
    )
    .first()
)
    if not schedule:
        raise HTTPException(
            status_code=404,
            detail="Schedule not found"
        )
    new_notification_log = Notification_Log( 
        schedule_id=notification.schedule_id,
        status=notification.status,
        message=notification.message
    )
    db.add(new_notification_log)
    db.commit()
    db.refresh(new_notification_log)
    return new_notification_log

@router.get("/", response_model=list[NotificationLogResponse])
def read_notification_logs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    notification_logs = db.query(Notification_Log).join(Schedule, Notification_Log.schedule_id == Schedule.id).filter(Schedule.user_id == current_user.id).all()
    return notification_logs

@router.delete("/{notification_log_id}", status_code=204)
def delete_notification_log(notification_log_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    notification_log = db.query(Notification_Log).join(Schedule, Notification_Log.schedule_id == Schedule.id).filter(Notification_Log.id == notification_log_id, Schedule.user_id == current_user.id).first()
    if not notification_log:
        raise HTTPException(status_code=404, detail="Notification log not found")
    db.delete(notification_log)
    db.commit()