# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.utils.translation import ugettext_lazy as _

ANDROID = "ANDROID"
IPHONE = "IPHONE"

DEVICE_TOKEN_DEVICES = (
    (ANDROID, _("Android")),
    (IPHONE, _("IPhone"))
)

EMAIL = "EMAIL"
SMS = "SMS"
PUSH = "PUSH"

NOTIFICATION_TYPE_CHOICES = (
    (EMAIL, _("Email Notification")),
    (SMS, _("SMS Notification")),
    (PUSH, _("Push Notification")),
)

ACCOUNTS_USER_REGISTER = "ACCOUNTS_USER_REGISTER"
ACCOUNTS_USER_LOGIN = "ACCOUNTS_USER_LOGIN"
ACCOUNTS_USER_FORGET_PASSWORD = "ACCOUNTS_USER_FORGET_PASSWORD"
ACCOUNTS_USER_UPDATE = "ACCOUNTS_USER_UPDATE"
ACCOUNTS_USER_PHONE_UPDATE = "ACCOUNTS_USER_PHONE_UPDATE"
ACCOUNT_USER_LOGIN_OTP = "ACCOUNT_USER_LOGIN_OTP"

ACTIVITY_CHOICES = (
    (ACCOUNTS_USER_REGISTER, _("Accounts User Register")),
    (ACCOUNTS_USER_LOGIN, _("Accounts User Login")),
    (ACCOUNTS_USER_FORGET_PASSWORD, _("Accounts User Forget Password")),
    (ACCOUNTS_USER_UPDATE, _("Accounts User Update")),
    (ACCOUNTS_USER_PHONE_UPDATE, _("Accounts User Phone Update")),
    (ACCOUNT_USER_LOGIN_OTP, _("Accounts User Login OTP")),
)
