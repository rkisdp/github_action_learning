# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.urls import path

# project imports
from accounts.apis import user


urlpatterns = [
    path(
        'register/',
        user.RegisterUser.as_view(),
        name="user_register_api"
    ),
    path(
        'me/',
        user.UserRetrieveUpdateAPIView.as_view(),
        name="user_get_update_api"
    ),
    path(
        'login/',
        user.CustomAuthToken.as_view(),
        name="login_api"
    ),
    path(
        'otp-login/request/',
        user.OTPRequestAuthToken.as_view(),
        name="otp_login_request_api"
    ),
    path(
        'otp-login/verify/',
        user.OTPVerifyAuthToken.as_view(),
        name="otp_login_verify_api"
    ),
]
