# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# project imports
from apps.accounts.models import Blog as BlogModel
from apps.accounts.tests.accounts_test_helper import populate_test_accounts_db

# Create your tests here.

faker = Faker("cz_CZ")


class TestBlog(APITestCase):
    def setUp(self):
        super().setUp()
        populate_test_accounts_db(model={"blog"})

    def test_blog_list(self):
        url = reverse("list_blog_api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_retrieve(self):
        def test_blog_retrieve_success(self):
            blog_obj = BlogModel.objects.first()
            url = reverse("blog_by_id_api", kwargs={"pk": blog_obj.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_blog_retrieve_not_found(self):
            url = reverse("blog_by_id_api", kwargs={"pk": 0})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        test_blog_retrieve_success(self)
        test_blog_retrieve_not_found(self)
