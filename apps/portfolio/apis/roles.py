# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.generics import ListAPIView

# project imports
from apps.portfolio.models import Role
from apps.portfolio.serializers.roles import RoleSerializer


class ListRolesView(ListAPIView):
    model = Role
    serializer_class = RoleSerializer

    def get_queryset(self):
        return self.model.objects.filter_is_delete().order_by("create_date")
