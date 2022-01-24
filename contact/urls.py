# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.urls import path

# project imports
from contact.apis import contact_form, social_links

urlpatterns = [
    path("social_links/", social_links.ListSocialLinkView.as_view(), name="social_links_list_api"),
    path("contact_form/", contact_form.CreateContactView.as_view(), name="add_contact_form_api"),
]
