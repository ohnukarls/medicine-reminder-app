from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    medication_name = Column(String, nullable=False)
    dosage = Column(String)
    instructions  = Column(String)

    user = relationship("User", back_populates="medications")