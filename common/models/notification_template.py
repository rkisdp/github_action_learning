# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from common import constants
from utils.core.models import TimeStampable
from common.managers.notification_template import NotificationTemplateManager, NotificationTemplateQuerySet 


class NotificationTemplate(TimeStampable):
    """
    Description of NotificationTemplate Model
    """

    name = models.CharField(
        verbose_name=_('Notification template name'),
        max_length=64
    )
    notification_type = models.CharField(
        verbose_name=_('Notification Type'),
        max_length=8,
        choices=constants.NOTIFICATION_TYPE_CHOICES,
    )
    subject = models.TextField(
        verbose_name=_('Notification Subject')
    )
    content = models.TextField(
        verbose_name=_('Notification Content')
    )

    objects = NotificationTemplateManager.from_queryset(NotificationTemplateQuerySet)()

    class Meta:
        app_label = 'common'
        verbose_name = _('Notification Template')
        verbose_name_plural = _('Notification Templates')
        indexes = [
            models.Index(fields=['notification_type']),
        ]

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
