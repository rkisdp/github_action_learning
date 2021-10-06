# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import uuid

# lib imports
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from accounts.managers.blog import BlogQueryset, BlogManager

USER = get_user_model()


def upload_to(instance, filename):
    path = f'blog/images/upload/'
    try:
        ext = filename.split('.')[-1]
    except IndexError:
        ext = filename
    filename = path + '{}/{}{}.{}'.format(instance.id, filename, uuid.uuid4().hex, ext)
    return filename


class Blog(TimeStampable):
    """
    Description of Blog Model
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=64,
        help_text=_('Title of the blog'),
    )
    author = models.ForeignKey(
        verbose_name=_('User'),
        to=USER,
        related_name='blog_author',
        on_delete=models.CASCADE,
        help_text=_('Author of the blog'),
        null=True, blank=True
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=upload_to,
    )
    text = models.TextField(
        verbose_name=_('Text')
    )
    extra_data = models.JSONField(
        verbose_name=_('Extra Data'),
        default=dict, blank=True,
        help_text=_('Pass more information here in extra data'),
    )

    objects = BlogManager.from_queryset(BlogQueryset)()

    class Meta:
        app_label = 'accounts'
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return f'id: {self.id} & title: {self.title} & author: {self.author}'

    def __unicode__(self):
        return f'id: {self.id} & title: {self.title} & author: {self.author}'
