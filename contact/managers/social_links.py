# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models

# project imports
from utils.core.managers import TimeStampableMixin


class SocialLinkQueryset(TimeStampableMixin):
    pass


class SocialLinkManager(models.Manager):
    def get_queryset(self):
        return SocialLinkQueryset(self.model, using=self._db)
