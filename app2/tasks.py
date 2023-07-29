from app2.celery_app import app
from datetime import datetime
import pika
from app2.config.pika_config import pika_config


@app.task(name="process_async_notify_task")
def process_async_notify_task():
    print(f"async notify task processed at {datetime.now()}")


@app.task(name="process_sync_notify_task")
def process_sync_notify_task(reply_to, correlation_id):
    msg = f"sync notify task processed at {datetime.now()}"
    pika_config.channel.basic_publish(
        exchange="",
        routing_key=reply_to,
        properties=pika.BasicProperties(correlation_id=correlation_id),
        body=msg,
    )
    print(msg)


@app.task(name="scheduled_task")
def scheduled_task():
    print(f"scheduled task processed at {datetime.now()}")
