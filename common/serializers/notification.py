# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import serializers

# project imports
from common.models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    def validate(self, data):
        data['user_id'] = self.context['request'].user.id
        return data

    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ('id', 'user')
        datetime_fields = ('create_date', 'modified_date')

