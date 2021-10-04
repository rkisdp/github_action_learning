# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.utils.translation import ugettext_lazy as _


SMS_TYPE = "SMS"
EMAIL_TYPE = "EMAIL"

TOKEN_TYPES = ((SMS_TYPE, _("sms")), (EMAIL_TYPE, _("email")))

VALID_NUMBER_OF_ATTEMPTS = 3
