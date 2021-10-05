# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# project imports
from portfolio.models import Project, Testimonial, Skill, Role


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('id', 'project_name')
    readonly_fields = ('create_date', 'modified_date')
    search_fields = ('id', 'project_name')


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportModelAdmin):
    list_display = ('id', 'review_name', 'designation')
    readonly_fields = ('create_date', 'modified_date')
    search_fields = ('id', 'review_name', 'designation')


@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'level')
    list_filter = ('level',)
    readonly_fields = ('create_date', 'modified_date')
    search_fields = ('id', 'name')


@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('create_date', 'modified_date')
    search_fields = ('id', 'name')

