from app2.config.app_config import RABBITMQ_HOST

broker_url = RABBITMQ_HOST
result_backend = "rpc://"
task_default_queue = "app2_default"
imports = ["app2.tasks"]
