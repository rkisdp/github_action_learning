
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from common.serializers import NotificationSerializers
from common.models import Notification


class ListNotificationView(ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    model = Notification
    serializer_class = NotificationSerializers

    def get_queryset(self):
        return self.model.objects.filter(
            user_id=self.request.user.id
        ).order_by('modified_date')


class GetDeleteNotificationView(RetrieveDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    model = Notification
    serializer_class = NotificationSerializers

    def get_object(self):
        return self.model.objects.get(
            pk=self.kwargs.get("pk"),
            user_id=self.request.user.id
        )
