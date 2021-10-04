# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
from contextlib import suppress
from typing import Optional


# project imports
from accounts.models import User as UserModel


def get_user(
        pk: Optional[int] = 0,
        username: Optional[str] = "",
        email: Optional[str] = "",
        phone: Optional[str] = "",
):
    """
    Get User

    Args:
        pk (int): id field in user table
        email (str): user email id
        username (str): user username
        phone (str): user phone number

    Returns
        :obj: User: User entity of UserModel object

    Raises:
        Exception: User Not Found
    """
    args = {}
    if pk:
        args["pk"] = pk
    if username:
        args["username"] = username
    if email:
        args["email"] = email
    if phone:
        args["phone"] = phone
    with suppress(UserModel.DoesNotExist):
        user = UserModel.objects.get(**args)
        return user
    return None
