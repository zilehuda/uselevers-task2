import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
