from celery import shared_task


@shared_task
def celery_test_task():
    for i in range(1000):
        print(i)
    return 'done'
