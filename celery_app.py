from celery import Celery

app = Celery(
    "app",
    broker="redis://localhost",
    backend="redis://localhost",
    include=["tasks"],
)

app.conf.result_expires = 20