from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from app.database import Base
from datetime import datetime

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True, index=True)
    schedule_id = Column(Integer, ForeignKey("schedules.id"), nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String)
    time = Column(DateTime, nullable=False)
    frequency = Column(String, default="daily")
    days_of_week = Column(String)
    is_active = Column(Boolean, default=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    last_sent_at = Column(DateTime)