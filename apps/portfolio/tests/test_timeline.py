# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestTimeline(APITestCase):
    def test_timeline_list_api(self):
        url = reverse("testimonial_list_api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
