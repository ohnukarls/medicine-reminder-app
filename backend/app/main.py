from fastapi import FastAPI
from app.database import Base, engine
from app.models import users, medications, notifications
from app.routers import auth, users, medications, notifications

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(medications.router)
app.include_router(notifications.router)

@app.get("/")
def root():
    return {"message": "Medicine Reminder API running"}