# python imports
from __future__ import unicode_literals

# project imports
from common.models import Notification as NotificationModel


def get_notification(pk: int, user_id: int, type: str):
    return NotificationModel.objects.get(pk=pk, user_id=user_id, type=type)
