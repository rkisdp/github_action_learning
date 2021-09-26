# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# lib imports
from django.db import models
from utils.core.managers import TimeStampableMixin


class TestimonialQueryset(TimeStampableMixin):
    pass


class TestimonialManager(models.Manager):
    def get_queryset(self):
        return TestimonialQueryset(self.model, using=self._db)
