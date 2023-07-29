from app1.config.app_config import RABBITMQ_HOST

broker_url = RABBITMQ_HOST
print("broker_url: ", broker_url)
result_backend = "rpc://"
task_default_queue = "app1_default"
imports = ["app1.tasks"]
