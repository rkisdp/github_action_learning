# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import uuid

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from portfolio import constants
from portfolio.managers.skills import SkillQueryset, SkillManager


def upload_to(instance, filename):
    path = f'skills/images/upload/'
    try:
        ext = filename.split('.')[-1]
    except IndexError:
        ext = filename
    filename = path + '{}/{}{}.{}'.format(instance.id, filename, uuid.uuid4().hex, ext)
    return filename


class Skill(TimeStampable):
    """
    Skill model description
    """
    name = models.CharField(
        verbose_name=_('Skill Name'),
        max_length=64
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=upload_to,
    )
    level = models.CharField(
        verbose_name=_('Level'),
        choices=constants.SKILL_TYPES,
        max_length=32,
        null=True, blank=True
    )
    extra_data = models.JSONField(
        verbose_name=_('extra data'),
        default=dict,
        null=True, blank=True
    )

    objects = SkillManager.from_queryset(SkillQueryset)()

    class Meta:
        app_label = 'portfolio'
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return f"id: {self.id} - skill: {self.name}"

    def __unicode__(self):
        return f"id: {self.id} - skill: {self.name}"

