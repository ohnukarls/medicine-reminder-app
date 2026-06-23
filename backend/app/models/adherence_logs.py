from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class Adherence_Log(Base):
    __tablename__ = "adherence_logs"

    id = Column(Integer, primary_key=True, index=True) 
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False)
    taken_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False)  # e.g., "taken", "missed", "late" 