# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.generics import ListAPIView

# project imports
from contact.models import SocialLink
from contact.serializers.social_link import SocialLinkSerializer


class ListSocialLinkView(ListAPIView):
    model = SocialLink
    serializer_class = SocialLinkSerializer

    def get_queryset(self):
        return self.model.objects.filter_is_delete().order_by('create_date')
