# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_jwt.settings import api_settings

# project imports
from accounts.serializers import UserSerializer

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'token': token.key,
            }, status.HTTP_201_CREATED
        )
