# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
from contextlib import suppress

# lib imports
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView

# project imports
from common.gateways import notification as notification_db_gateway
from common.models import Notification
from common.serializers import NotificationSerializer


class ListNotificationView(ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    model = Notification
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            user_id=self.request.user.id
        ).order_by('modified_date')


class GetDeleteNotificationView(RetrieveDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    model = Notification
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        with suppress(Notification.DoesNotExist):
            notification_entity = notification_db_gateway.get_notification(
                pk=kwargs.get('pk'), user_id=self.request.user.id, type="PUSH"
            )
            serializer = self.serializer_class(notification_entity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Resource does not exist"}, status=status.HTTP_404_NOT_FOUND)
