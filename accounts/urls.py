from django.urls import path
from . import apis


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
]
