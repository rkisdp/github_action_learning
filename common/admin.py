# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# project imports
from common.models import Notification, NotificationTemplate, ActivityConfig


@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
    list_filter = ('type',)
    list_display = ('id', 'type', 'user_id')
    readonly_fields = ('create_date', 'modified_date')
    search_fields = ('id', 'user_id', 'subject', 'content')


@admin.register(ActivityConfig)
class ActivityConfigAdmin(ImportExportModelAdmin):
    list_filter = ('activity_name',)
    list_display = ('id', 'activity_name')
    search_fields = ('id', 'activity_name')
    readonly_fields = ('create_date', 'modified_date')


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(ImportExportModelAdmin):
    search_fields = ('id', 'name', )
    list_filter = ('notification_type',)
    list_display = ('id', 'notification_type', 'name')
    readonly_fields = ('create_date', 'modified_date')
