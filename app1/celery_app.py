from celery import Celery

app = Celery("app1")
app.config_from_object("app1.config.celeryconfig")
