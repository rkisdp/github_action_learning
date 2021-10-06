# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import uuid

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project imports
from utils.core.models import TimeStampable
from contact.managers.social_links import SocialLinkQueryset, SocialLinkManager


def upload_to(instance, filename):
    path = f'social_link/images/upload/'
    try:
        ext = filename.split('.')[-1]
    except IndexError:
        ext = filename
    filename = path + '{}/{}{}.{}'.format(instance.id, filename, uuid.uuid4().hex, ext)
    return filename


class SocialLink(TimeStampable):
    """
    Description of SocialLink Model
    """
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=32
    )
    url = models.URLField(
        verbose_name=_('URL'),
        null=True, blank=True
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=upload_to,
    )

    objects = SocialLinkManager.from_queryset(SocialLinkQueryset)()

    class Meta:
        app_label = 'contact'
        verbose_name = _('Social link')
        verbose_name_plural = _('Social links')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
