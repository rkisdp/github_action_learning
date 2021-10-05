# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import json

# lib imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# project imports
from accounts.serializers import UserSerializer
from accounts.gateways import user as user_db_gateway
from accounts.gateways import verification_token as verification_token_db_gateway


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


class OTPRequestAuthToken(generics.CreateAPIView):
    def post(self, request, **kwargs):
        body = json.loads(request.body)
        user = user_db_gateway.get_user(phone=body.get('phone'))
        verification_token_db_gateway.create_verification_token(
            data={'user_id': user.id, 'token_type': 'SMS'}
        )
        return Response({}, status.HTTP_201_CREATED)


class OTPVerifyAuthToken(generics.CreateAPIView):
    def post(self, request, **kwargs):
        body = json.loads(request.body)
        otp, phone = body.get('otp'), body.get('phone')
        token_type = body.get('type', 'SMS')
        user = user_db_gateway.get_user(phone=phone)
        verification_token = verification_token_db_gateway.get_user_valid_token(
            user_id=user.id, token_type=token_type
        )
        if verification_token and verification_token.token == otp:
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
        else:
            return Response(
                {'status': 'invalid user token'},
                status.HTTP_400_BAD_REQUEST
            )
