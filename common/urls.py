# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.urls import path

# project imports
from common.apis import notification

urlpatterns = [
    path(
        "notifications/",
        notification.ListNotificationView.as_view(),
        name="notifications_list_api"
    ),
    path(
        "notification/<int:pk>/",
        notification.GetDeleteNotificationView.as_view(),
        name="notification_api"
    ),
    path(
        "notification/register-device/",
        notification.RegisterDeviceView.as_view(),
        name="register_device_api"
    )
]
