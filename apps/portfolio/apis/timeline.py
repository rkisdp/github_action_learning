# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.generics import ListAPIView

# project imports
from apps.portfolio.models import Timeline
from apps.portfolio.serializers.timeline import TimelineSerializer


class ListTestimonialsView(ListAPIView):
    model = Timeline
    serializer_class = TimelineSerializer

    def get_queryset(self):
        return self.model.objects.filter_is_delete().order_by("create_date")
