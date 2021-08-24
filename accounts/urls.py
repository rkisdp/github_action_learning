from django.urls import path
from . import views

urlpatterns = [
    path('', views.testv2, name="celery_test_task"),
    path('accounts/', views.test, name="celery_test_task"),
]
