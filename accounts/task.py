from celery import shared_task


@shared_task
def celery_test_task():
    return 'done'
