# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

faker = Faker("cz_CZ")


class TestContactForm(APITestCase):
    def test_add_contact_form_api(self):
        url = reverse("add_contact_form_api")
        fake_data = {
            "name": faker.name(),
            "email": faker.email(),
            "contact_number": f"{+91} {faker.phone_number()}",
            "message": faker.text(),
        }
        response = self.client.post(url, data=fake_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
