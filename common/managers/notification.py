# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# lib imports
from django.db import models
from utils.core.managers import TimeStampableMixin


class NotificationQueryset(TimeStampableMixin):

    def select_relate_user(self):
        return self.select_related("user")


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQueryset(self.model, using=self._db)
