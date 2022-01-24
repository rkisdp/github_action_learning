# -*- coding: utf-8 -*-
# python import
from __future__ import unicode_literals

import uuid

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from portfolio.managers.testimonials import (TestimonialManager,
                                             TestimonialQueryset)
from utils.core.models import TimeStampable


def upload_to(instance, filename):
    path = f"images/upload/"
    try:
        ext = filename.split(".")[-1]
    except IndexError:
        ext = filename
    filename = path + "{}/{}{}.{}".format(instance.id, filename, uuid.uuid4().hex, ext)
    return filename


class Testimonial(TimeStampable):
    """
    Testimonial model description
    """

    quote = models.CharField(verbose_name=_("Quote"), max_length=64)
    image = models.ImageField(verbose_name=_("image"), upload_to=upload_to, null=True, blank=True)
    review_name = models.CharField(verbose_name=_("Review's Name"), max_length=64)
    review = models.TextField(verbose_name=_("Review"))
    designation = models.CharField(
        verbose_name=_("Designation"), max_length=64, null=True, blank=True
    )
    organisation = models.CharField(
        verbose_name=_("Organisation"), max_length=64, null=True, blank=True
    )

    objects = TestimonialManager.from_queryset(TestimonialQueryset)()

    class Meta:
        app_label = "portfolio"
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return f"id: {self.id} - review name: {self.review_name}"

    def __unicode__(self):
        return f"id: {self.id} - review name: {self.review_name}"
