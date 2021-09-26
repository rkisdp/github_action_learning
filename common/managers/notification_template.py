# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# lib imports
from django.db import models

# project imports
from utils.core.managers import TimeStampableMixin


class NotificationTemplateQuerySet(TimeStampableMixin):
    def filter_notification_type(self, notification_type):
        return self.filter(notification_type=notification_type)

    def filter_name(self, name):
        return self.filter(name=name)


class NotificationTemplateManager(models.Manager):
    def get_queryset(self):
        return NotificationTemplateQuerySet(self.model, using=self._db)
