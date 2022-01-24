# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class DeviceTypeChoice(TextChoices):
    ANDROID = "ANDROID", _("Android")
    IPHONE = "IPHONE", _("IPhone")


class NotificationTypeChoice(TextChoices):
    EMAIL = "EMAIL", _("Email Notification")
    SMS = "SMS", _("SMS Notification")
    PUSH = "PUSH", _("Push Notification")


class ActivityChoice(TextChoices):
    ACCOUNTS_USER_REGISTER = "ACCOUNTS_USER_REGISTER", _("Accounts User Register")
    ACCOUNTS_USER_LOGIN = "ACCOUNTS_USER_LOGIN", _("Accounts User Login")
    ACCOUNTS_USER_FORGET_PASSWORD = (
        "ACCOUNTS_USER_FORGET_PASSWORD",
        _("Accounts User Forget Password"),
    )
    ACCOUNTS_USER_UPDATE = "ACCOUNTS_USER_UPDATE", _("Accounts User Update")
    ACCOUNTS_USER_PHONE_UPDATE = "ACCOUNTS_USER_PHONE_UPDATE", _("Accounts User Phone Update")
    ACCOUNT_USER_LOGIN_OTP = "ACCOUNT_USER_LOGIN_OTP", _("Accounts User Login OTP")
