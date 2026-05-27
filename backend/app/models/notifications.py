from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    notification_type = Column(String)
    sent_at = Column(DateTime, default=datetime.utcnow)
