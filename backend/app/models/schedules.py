from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class Schedule(Base):
    __tablename__ = "schedules" 

    id = Column(Integer, primary_key=True, index=True)    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to users table
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False)  # Foreign key to medications table   
    recurrence_pattern = Column(String, nullable=False)  # e.g., "daily", "weekly", "every 8 hours"
    reminder_time = Column(DateTime, nullable=False)  # Time of day for the reminder
    timezone = Column(String, nullable=False)  # Timezone for the reminder time

