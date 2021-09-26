from django.urls import path
from common.apis import notification

urlpatterns = [
    path(
        "notifications/",
        notification.ListNotificationView.as_view(),
        name="notifications_list_api"
    ),
    path(
        "notifications/<int:pk>/",
        notification.GetDeleteNotificationView.as_view(),
        name="notification_list_api"
    )
]
