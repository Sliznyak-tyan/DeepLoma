from DeepLoma.celery import app


@app.task
def slave():
    print('deep dark fantasy')


slave.apply_async()
