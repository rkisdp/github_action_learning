# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.urls import path

# project imports
from portfolio.apis import testimonials

urlpatterns = [
    path(
        "testimonials/",
        testimonials.ListTestimonialsView.as_view(),
        name="testimonial_list_api"
    ),
]
