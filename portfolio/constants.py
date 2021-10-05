# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.utils.translation import ugettext_lazy as _


ADVANCE_TYPE = 'ADVANCE'
INTERMEDIATE_TYPE = 'INTERMEDIATE'
BEGINNER_TYPE = 'BEGINNER'


SKILL_TYPES = (
    (ADVANCE_TYPE, _('Advance')),
    (INTERMEDIATE_TYPE, _('Intermediate')),
    (BEGINNER_TYPE, _('Beginner'))
)