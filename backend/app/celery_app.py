import os

from celery import Celery


def get_celery_broker_url() -> str:
    return os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")


def get_celery_result_backend() -> str:
    return os.environ.get("CELERY_RESULT_BACKEND", get_celery_broker_url())


celery_app = Celery(
    "medicine_reminder",
    broker=get_celery_broker_url(),
    backend=get_celery_result_backend(),
    include=["app.tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_default_queue="default",
    task_routes={
        "app.tasks.*": {"queue": "default"},
    },
    beat_schedule={
        "check-medication-reminders": {
            "task": "app.tasks.check_medication_reminders",
            "schedule": 60.0,  
        },
    },
)

if __name__ == "__main__":
    celery_app.start()
