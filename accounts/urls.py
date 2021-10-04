# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# lib imports
from django.urls import path

# project imports
from accounts import apis


urlpatterns = [
    path(
        'register/',
        apis.RegisterUser.as_view(),
        name="user_register_api"
    ),
    path(
        'me/',
        apis.UserRetrieveUpdateAPIView.as_view(),
        name="user_get_update_api"
    ),
    path(
        'login/',
        apis.CustomAuthToken.as_view(),
        name="login_api"
    ),
    path(
        'otp-login/request/',
        apis.OTPRequestAuthToken.as_view(),
        name="otp_login_request_api"
    ),
    path(
        'otp-login/verify/',
        apis.OTPVerifyAuthToken.as_view(),
        name="otp_login_verify_api"
    ),
]
