from app.celery_app import celery_app
from app.database import SessionLocal
from app.models.schedules import Schedule
from app.models.notification_logs import Notification_Log
from datetime import datetime, timezone
from sqlalchemy import func

@celery_app.task
def test_task():
    return "Celery is working!"

@celery_app.task
def check_medication_reminders():
    db = SessionLocal()
    try: ##npm create vite@latest . -- --template react-ts
        now = datetime.now(timezone.utc).replace(second=0, microsecond=0)

        due_schedules = (db.query(Schedule).filter(func.date_trunc("minute", Schedule.reminder_time) == now).all())

        for schedule in due_schedules:            
            existing = (db.query(Notification_Log).filter(
                Notification_Log.schedule_id == schedule.id, Notification_Log.status == "pending",).first()
                )

            if existing:
                continue

            notification = Notification_Log(
                            schedule_id=schedule.id,
                            status="pending",
                            message="Medication reminder is due.",
                        )
        
            db.add(notification)

        db.commit()
        
        return f"Found {len(due_schedules)} due medication reminders."

    except Exception:
        db.rollback()
        raise
        

    finally:
        db.close()