# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.urls import path

# project imports
from portfolio.apis import (
    testimonials, projects, skills, rolls, timeline
)

urlpatterns = [
    path(
        'testimonials/',
        testimonials.ListTestimonialsView.as_view(),
        name='testimonial_list_api'
    ),
    path(
        'projects/',
        projects.ListProjectsView.as_view(),
        name='projects_list_api'
    ),
    path(
        'skills/',
        skills.ListSkillsView.as_view(),
        name='skills_list_api'
    ),
    path(
        'roles/',
        rolls.ListRolesView.as_view(),
        name='roles_list_api'
    ),
    path(
        'timeline/',
        timeline.ListTestimonialsView.as_view(),
        name='timeline_list_api'
    ),
]
