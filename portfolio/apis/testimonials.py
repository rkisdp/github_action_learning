# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# lib imports
from rest_framework.generics import ListAPIView

# project imports
from portfolio.models import Testimonial
from portfolio.serializers.testimonials import TestimonialSerializers


class ListTestimonialsView(ListAPIView):
    model = Testimonial
    serializer_class = TestimonialSerializers

    def get_queryset(self):
        return self.model.objects.all()

