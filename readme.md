# task2

This repository contains the code for task2 RabbitMQ and Celery (Public) (https://uselevers.notion.site/RabbitMQ-and-Celery-Public-674766bccbdd4f678cc664651db08463)

# Installation

To install and run the app using Docker Compose, follow these steps:

1. Create a new file named `.env` from `.env.example` using a text editor:

```bash
cp .env.example .env
```

2. Open the .env file in a text editor and define the necessary environment variables.
   These variables are used to configure the application. You can use the following content

```bash
RABBITMQ_HOST=amqp://guest:guest@rabbitmq:5672/
```

3. Build and start the Docker containers using Docker Compose:

```bash
docker-compose up -d
```

This command will build the Docker image and start the containers in detached mode.

4. Verify that the containers are running:

```bash
docker-compose ps
```

You should see the running containers listed

- To access API doc: http://localhost:8000/docs
- To access rabbitmq dashboard: http://localhost:15672/

# APIs
- http://localhost:8000/notify
- http://localhost:8000/notify-sync

You can use tools like cURL, Postman, or any other HTTP client to interact with the API endpoints.

# Improvements:

Use better container startup strategy and wait for rabbitmq, right now it is keep restarting till rabbitmq started. 
Also disable heartbeat from pika for rabbitmq
