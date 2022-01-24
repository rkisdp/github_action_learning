# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from contextlib import suppress

# lib imports
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

# project imports
from accounts import messages
from accounts.gateways import blog as blog_db_gateway
from accounts.models import Blog
from accounts.serializers.blog import BlogSerializer


class ListBlogsView(ListAPIView):
    model = Blog
    serializer_class = BlogSerializer

    def get_queryset(self):
        return self.model.objects.filter_is_delete().order_by("create_date")


class GetBlogView(RetrieveAPIView):
    model = Blog
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        with suppress(Blog.DoesNotExist):
            blog_entity = blog_db_gateway.get_blog_by_pk(pk=kwargs.get("pk"))
            serializer = self.serializer_class(blog_entity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": messages.NO_RESOURCE}, status=status.HTTP_404_NOT_FOUND)
