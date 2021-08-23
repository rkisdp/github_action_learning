from django.shortcuts import render
from django.http import HttpResponse
from .task import celery_test_task
# Create your views here.

def test(request):
    celery_test_task.delay()
    return HttpResponse('Done')
