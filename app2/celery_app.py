from celery import Celery
from celery.schedules import crontab

app = Celery("app2")
app.config_from_object("app2.config.celeryconfig")

app.conf.beat_schedule = {
    "scheduled_task_for_every_3_minute": {
        "task": "scheduled_task",
        "schedule": crontab(minute="*/3"),
    },
}
