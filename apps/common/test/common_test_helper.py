# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.authtoken.models import Token

# project imports
from apps.accounts.models import User as UserModel
from apps.common.models import Notification as NotificationModel


def create_user():
    return UserModel.objects.create_user(
        username="TestUser",
        first_name="Test",
        last_name="User",
        phone="00000000",
        email="test@test.com",
        password="testpassword",
    )


def create_notification():
    test_user = create_user()
    return (
        NotificationModel.objects.create(notification="testnotification", user_id=test_user.id),
        test_user,
    )


def populate_test_db(model: set):
    if "notification" in model:
        notification, user = create_notification()
        token = Token.objects.get_or_create(user=user)
    return token
