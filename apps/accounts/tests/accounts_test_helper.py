# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.authtoken.models import Token

# project imports
from apps.accounts.models import Blog as BlogModel
from apps.accounts.models import User as UserModel
from apps.accounts.models import VerificationToken as VerificationTokenModel


def create_blog():
    BlogModel.objects.create(title="Test Blog", text="Test Text")


def create_user():
    UserModel.objects.create_user(
        username="TestUser",
        first_name="Test",
        last_name="User",
        phone="00000000",
        email="test@test.com",
        password="testpassword",
    )


def create_token():
    user = UserModel.objects.get(username="TestUser")
    Token.objects.get_or_create(user=user)


def create_verification_token():
    user = UserModel.objects.get(username="TestUser")
    VerificationTokenModel.objects.create(user_id=user.id, token_type="SMS", is_valid=True)


def populate_test_accounts_db(model: set):

    if "blog" in model:
        create_blog()

    if "user" in model:
        create_user()
        create_token()
        create_verification_token()

    return True
