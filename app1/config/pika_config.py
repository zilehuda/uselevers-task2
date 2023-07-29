from dataclasses import dataclass
from functools import lru_cache

import pika

from app1.config.app_config import RABBITMQ_HOST


@dataclass
class PikaConfig:
    rabbitmq_host: str = RABBITMQ_HOST
    async_queue: str = "async_queue"  # we can move it to .env as well
    sync_queue: str = "sync_queue"  # we can move it to .env as well
    queues: list = None
    channel: pika.adapters.BlockingConnection = None

    def __post_init__(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(self.rabbitmq_host)
        )
        self.channel = self.connection.channel()
        self.queues = [self.async_queue, self.sync_queue]


@lru_cache
def get_pika_config():
    return PikaConfig()


pika_config = get_pika_config()
