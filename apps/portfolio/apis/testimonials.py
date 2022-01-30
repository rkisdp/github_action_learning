# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.generics import ListAPIView

# project imports
from apps.portfolio.models import Testimonial
from apps.portfolio.serializers.testimonials import TestimonialSerializer


class ListTestimonialsView(ListAPIView):
    model = Testimonial
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return self.model.objects.filter_is_delete().order_by("create_date")
