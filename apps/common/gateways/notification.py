# python imports
from __future__ import unicode_literals

# project imports
from apps.common.models import Notification as NotificationModel


def get_notification(pk: int, user_id: int, type: str):
    return NotificationModel.objects.get(pk=pk, user_id=user_id, type=type)


def filter_by_user_and_type(user_id: int, type: str):
    return NotificationModel.objects.filter_by_user_and_type(user_id=user_id, type=type)
