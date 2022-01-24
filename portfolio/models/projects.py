# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from portfolio.managers.projects import ProjectManager, ProjectQueryset
from utils.core.models import TimeStampable


class Project(TimeStampable):
    """
    Project model description
    """

    project_name = models.CharField(verbose_name=_("Project Name"), max_length=64)
    url = models.URLField(verbose_name=_("URL"), max_length=512)
    description = models.TextField(verbose_name=_("Description"))
    extra_data = models.JSONField(verbose_name=_("extra data"), default=dict, null=True, blank=True)

    objects = ProjectManager.from_queryset(ProjectQueryset)()

    class Meta:
        app_label = "portfolio"
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return f"id: {self.id} - project_name: {self.project_name}"

    def __unicode__(self):
        return f"id: {self.id} - project_name: {self.project_name}"
