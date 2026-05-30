from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.notifications import Notification
from app.models.users import User
from app.schemas.notifications import (
    NotificationCreate,
    NotificationResponse
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/notifications",        
    tags=["notifications"]
)

@router.get("/", response_model=list[NotificationResponse])
def read_notifications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    notifications = db.query(Notification).filter(Notification.user_id == current_user.id).all()
    return notifications

@router.delete("/{notification_id}", status_code=204)
def delete_notification(notification_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    notification = db.query(Notification).filter(Notification.id == notification_id, Notification.user_id == current_user.id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(notification)
    db.commit()