# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from contact.managers.contact_form import (ContactFormManager,
                                           ContactFormQueryset)
# project imports
from utils.core.models import TimeStampable


class ContactForm(TimeStampable):
    """
    Description of ContactForm Model
    """

    name = models.CharField(verbose_name=_("Name"), max_length=32)
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)
    contact_number = models.CharField(
        verbose_name=_("Contact number"), max_length=32, null=True, blank=True
    )
    message = models.TextField(verbose_name=_("Message"))

    objects = ContactFormManager.from_queryset(ContactFormQueryset)()

    class Meta:
        app_label = "contact"
        verbose_name = _("Contact me form")
        verbose_name_plural = _("Contact me forms")

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email
