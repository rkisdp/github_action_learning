# -*- coding: utf-8 -*-
# Python imports
from __future__ import unicode_literals
from typing import Dict
import json

# lib imports
from requests import request
from django.conf import settings

# ORM imports
from common.models import DeviceToken


def push(user_id: int, notification_data: Dict) -> None:
    """
    Used to send push notification

    Args:
        user_id (int): user id
        notification_data: notification body containing data, title and body

    Returns:
        None
    """
    url = settings.FCM_HOST
    devices = DeviceToken.objects.filter(user_id=user_id).values_list(
        "pk", flat=True
    )

    payload = {
        "registration_ids": list(devices),
        "notification": {
            "sound": "default",
            "body": notification_data.get("body"),
            "title": notification_data.get("title"),
            "content_available": True,
            "priority": "high",
        },
        "data": {"default": notification_data.get("data", "")},
    }
    request(
        method="POST",
        url=url,
        data=json.dumps(payload),
        headers={
            "Authorization": settings.FCM_SERVER_TOKEN,
            "Content-type": "application/json",
        },
    )
