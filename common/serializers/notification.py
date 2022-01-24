# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import serializers

# project imports
from common.models import DeviceToken, Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
        read_only_fields = ("id", "user")
        datetime_fields = ("create_date", "modified_date")


class DeviceTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceToken
        fields = "__all__"
        datetime_fields = ("create_date", "modified_date")
