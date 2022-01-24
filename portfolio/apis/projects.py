# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.generics import ListAPIView

# project imports
from portfolio.models import Project
from portfolio.serializers.projects import ProjectSerializer


class ListProjectsView(ListAPIView):
    model = Project
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.model.objects.filter_is_delete().order_by("create_date")
