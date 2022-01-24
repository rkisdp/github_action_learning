# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

import json

import requests
# lib imports
from django.conf import settings


def fcm_send_push(device_id: str, **kwargs):
    """
    push notifications need arn for platform device

    Args:
        device_id (str): device id of user device
        kwargs (dict): body and title of

    Return:
        fcm response
    """
    fcm_url = "https://fcm.googleapis.com/fcm/send"
    fcm_server_key = settings.FCM_SERVER_KEY
    payload = {
        "to": device_id,
        "notification": {
            "sound": "default",
            "body": kwargs.get("body"),
            "title": kwargs.get("title"),
            "content_available": True,
            "priority": "high",
        },
        "data": {"type": kwargs.get("data", "")},
    }
    response = requests.request(
        method="POST",
        url=fcm_url,
        data=json.dumps(payload),
        headers={"Authorization": "key=" + fcm_server_key, "Content-type": "application/json"},
    )
    return response.json()
