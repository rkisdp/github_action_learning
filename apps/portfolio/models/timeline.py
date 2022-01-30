# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

import uuid

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from apps.portfolio.managers.timeline import TimelineManager, TimelineQueryset
from utils.core.models import TimeStampable


def upload_to(instance, filename):
    path = f"timeline/images/upload/"
    try:
        ext = filename.split(".")[-1]
    except IndexError:
        ext = filename
    filename = path + "{}/{}{}.{}".format(instance.id, filename, uuid.uuid4().hex, ext)
    return filename


class Timeline(TimeStampable):
    """
    Timeline model description
    """

    title = models.CharField(verbose_name=_("Timeline title"), max_length=64)
    image = models.ImageField(verbose_name=_("Image"), upload_to=upload_to)
    text = models.TextField(verbose_name=_("Text"), null=True, blank=True)
    from_date = models.DateField(verbose_name=_("From date"), null=True, blank=True)
    to_date = models.DateField(verbose_name=_("To date"), null=True, blank=True)

    objects = TimelineManager.from_queryset(TimelineQueryset)()

    class Meta:
        app_label = "portfolio"
        verbose_name = _("Timeline")
        verbose_name_plural = _("Timeline")

    def __str__(self):
        return f"id: {self.id} - name: {self.title}"

    def __unicode__(self):
        return f"id: {self.id} - name: {self.title}"
