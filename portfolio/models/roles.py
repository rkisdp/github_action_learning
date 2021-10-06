# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from portfolio.managers.roles import RoleQueryset, RoleManager


class Role(TimeStampable):
    """
    Role model description
    """
    name = models.CharField(
        verbose_name=_('Role name'),
        max_length=64
    )

    objects = RoleManager.from_queryset(RoleQueryset)()

    class Meta:
        app_label = 'portfolio'
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return f"id: {self.id} - Role: {self.name}"

    def __unicode__(self):
        return f"id: {self.id} - Role: {self.name}"

