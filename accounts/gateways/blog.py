# python imports
from __future__ import unicode_literals

# project imports
from accounts.models import Blog as BlogModel


def get_blog_by_pk(pk: int):
    return BlogModel.objects.get_by_id(obj_id=pk)
