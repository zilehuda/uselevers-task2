from app1.config.pika_config import pika_config


class PikaService:
    @staticmethod
    def basic_public(routing_key: str, body: str = ""):
        pika_config.channel.queue_declare(queue=routing_key)

        pika_config.channel.basic_publish(
            exchange="", routing_key=routing_key, body=body
        )
