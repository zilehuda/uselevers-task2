import sys
import os

# Get the parent directory of app1 (the outer directory)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print("parent: ", parent_dir)
# Add the parent directory to the Python path
sys.path.append(parent_dir)

import logging
from tasks import process_async_notify_task, process_sync_notify_task
from app2.config.pika_config import pika_config

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Connect to RabbitMQ and consume messages
def consumer():
    for queue in pika_config.queues:
        pika_config.channel.queue_declare(queue=queue)

    def callback(ch, method, props, body):
        routing_key = method.routing_key
        logging.info("Received message from queue: %s", routing_key)

        if routing_key == pika_config.async_queue:
            logging.info("Processing async notify task.")
            process_async_notify_task.delay()

        if routing_key == pika_config.sync_queue:
            logging.info("Processing sync notify task.")
            process_sync_notify_task.delay(props.reply_to, props.correlation_id)

        logging.info("Processing completed")

    for queue in pika_config.queues:
        pika_config.channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True
        )

    logging.info("Waiting for messages from app1...")
    pika_config.channel.start_consuming()


if __name__ == "__main__":
    consumer()
