from fastapi import FastAPI
from app.database import Base, engine
from app.models import users, medications, notification_logs, adherence_logs, schedules
from app.routers import auth, users, medications, notification_logs, adherence_logs, schedules

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(medications.router)
app.include_router(notification_logs.router)
app.include_router(adherence_logs.router)
app.include_router(schedules.router)        
@app.get("/")
def root():
    return {"message": "Medicine Reminder API running"}