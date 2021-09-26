# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# project imports
from accounts.managers.user import UserManager, UserQuerySet


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model
    """
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=256,
        null=True,
        blank=True
    )
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=256,
        unique=True
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=128,
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=128,
        db_index=True
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=128,
        null=True,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_('Designates whether the user \
            can log into this admin site.')
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_('Designates whether this user \
            should be treated as active. \
            Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        default=timezone.now
    )

    objects = UserManager.from_queryset(UserQuerySet)()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        indexes = [
            models.Index(fields=['email', 'username', 'phone']),
        ]
        ordering = ('-id',)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __unicode__(self):
        return f'{self.username} - {self.full_name}'

    def __str__(self):
        return f'{self.username} - {self.full_name}'



