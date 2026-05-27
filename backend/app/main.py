from fastapi import FastAPI
from app.database import Base, engine
from app.models import users
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Medicine Reminder API running"}