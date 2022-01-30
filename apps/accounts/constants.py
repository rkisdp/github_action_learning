# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class TokenType(TextChoices):
    SMS_TYPE = "SMS", _("sms")
    EMAIL_TYPE = "EMAIL", _("email")


VALID_NUMBER_OF_ATTEMPTS = 3
