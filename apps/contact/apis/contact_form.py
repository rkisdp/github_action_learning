# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import generics
from rest_framework.permissions import AllowAny

# project imports
from apps.contact.serializers.contact_form import ContactFormSerializer


class CreateContactView(generics.CreateAPIView):
    serializer_class = ContactFormSerializer
    permission_classes = (AllowAny,)
