from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class Notification_Log(Base):
    __tablename__ = "notifications_logs"

    id = Column(Integer, primary_key=True, index=True)
    schedule_id=Column(Integer, ForeignKey("schedules.id"), nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), nullable=False)
    message = Column(String, nullable=False)
