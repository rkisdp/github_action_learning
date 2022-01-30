# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.generics import ListAPIView

# project imports
from apps.portfolio.models import Skill
from apps.portfolio.serializers.skills import SkillSerializer


class ListSkillsView(ListAPIView):
    model = Skill
    serializer_class = SkillSerializer

    def get_queryset(self):
        return self.model.objects.filter_is_delete().order_by("create_date")
