# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# project imports
from contact.models import ContactForm, SocialLink


@admin.register(ContactForm)
class ContactFormAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "email", "contact_number")
    readonly_fields = ("create_date", "modified_date")
    search_fields = ("id", "name", "email", "contact_number")


@admin.register(SocialLink)
class SocialLinkAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")
    readonly_fields = ("create_date", "modified_date")
    search_fields = ("id", "name")
