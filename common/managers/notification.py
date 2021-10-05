# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from utils.core.managers import TimeStampableMixin


class NotificationQueryset(TimeStampableMixin):

    def filter_by_user_and_type(self, user_id: int, type: str = 'PUSH'):
        return self.filter(user_id=user_id, type=type)

    def select_relate_user(self):
        return self.select_related("user")


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQueryset(self.model, using=self._db)
