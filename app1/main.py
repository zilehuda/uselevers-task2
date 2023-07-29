from fastapi import FastAPI

from app1 import tasks
from app1.config.pika_config import PikaConfig
from app1.services.pika_service import PikaService

app = FastAPI()


@app.get("/notify")
def notify():
    PikaService.basic_public(PikaConfig.async_queue)
    return {"message": "/notify API called"}


@app.get("/notify-sync")
async def notify_sync():
    task = tasks.call_sync_notify_task.delay()
    response = task.get()
    return {"message: ": response}
