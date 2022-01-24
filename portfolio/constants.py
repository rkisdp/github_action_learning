# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class SKillType(TextChoices):
    ADVANCE_TYPE = "ADVANCE", _("Advance")
    INTERMEDIATE_TYPE = "INTERMEDIATE", _("Intermediate")
    BEGINNER_TYPE = "BEGINNER", _("Beginner")
