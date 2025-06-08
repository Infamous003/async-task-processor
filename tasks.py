from celery_app import app
from time import sleep

@app.task
def sayHi():
    sleep(30)
    return "Hi"
