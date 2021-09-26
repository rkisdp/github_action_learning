from __future__ import unicode_literals

from django.db import models


class TimeStampableMixin(models.QuerySet):

    def filter_ids(self, ids: list):
        return self.filter(id__in=ids)

    def get_by_id(self, obj_id: int):
        return self.get(id=obj_id)

    def filter_is_active(self, is_active: bool = True):
        return self.filter(is_active=is_active)

    def filter_is_delete(self, is_delete: bool = False):
        return self.filter(is_delete=is_delete)
