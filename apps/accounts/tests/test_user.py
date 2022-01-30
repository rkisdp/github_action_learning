# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

import uuid

# lib imports
from faker import Faker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# project imports
from apps.accounts.gateways import user as user_db_gateway
from apps.accounts.gateways import \
    verification_token as verification_token_db_gateway
from apps.accounts.tests.accounts_test_helper import populate_test_accounts_db

# Create your tests here.

faker = Faker("cz_CZ")


class TestUser(APITestCase):

    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    phone = f"{+91} {faker.phone_number()}"
    password = faker.password()
    username = faker.user_name()

    def setUp(self):
        super().setUp()
        populate_test_accounts_db(model={"user"})

    def test_register_user(self):
        url = reverse("user_register_api")

        def test_register_user_success(self):
            fake_user_data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "phone": self.phone,
                "password": self.password,
                "username": self.username,
            }
            response = self.client.post(url, data=fake_user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_register_invalid_user(self):
            fake_user_data = {"first_name": self.first_name, "last_name": self.last_name}
            response = self.client.post(url, data=fake_user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        test_register_user_success(self)
        test_register_invalid_user(self)

    def test_user_otp_request(self):
        url = reverse("otp_login_request_api")

        def test_user_otp_request_success(self):
            user = user_db_gateway.get_user(username="TestUser")
            fake_user_data = {"phone": user.phone}
            response = self.client.post(url, data=fake_user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_user_otp_request_invalid_request(self):
            fake_user_data = {"phone": f"{+91}{faker.phone_number()}"}
            response = self.client.post(url, data=fake_user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        test_user_otp_request_success(self)
        test_user_otp_request_invalid_request(self)

    def test_otp_verify(self):
        url = reverse("otp_login_verify_api")

        def test_otp_verify_success(self):
            user = user_db_gateway.get_user(username="TestUser")
            verification_token = verification_token_db_gateway.get_user_valid_token(
                user_id=user.id, token_type="SMS"
            )
            fake_user_data = {"phone": user.phone, "otp": verification_token.token}
            response = self.client.post(url, data=fake_user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_otp_verify_denied(self):
            user = user_db_gateway.get_user(username="TestUser")
            fake_user_data = {
                "phone": user.phone,
                "otp": str(abs(hash(f"{uuid.uuid4()}")) % (10 ** 4)),
            }
            response = self.client.post(url, data=fake_user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        test_otp_verify_success(self)
        test_otp_verify_denied(self)

    def test_user_login_password(self):
        url = reverse("login_api")

        def test_user_login_success(self):
            user_data = {"email": "test@test.com", "password": "testpassword"}
            response = self.client.post(url, data=user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_user_login_denied(self):
            fake_user_data = {"email": self.email, "password": faker.password()}
            response = self.client.post(url, data=fake_user_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        test_user_login_success(self)
        test_user_login_denied(self)

    def test_user_retrieve_update(self):
        url = reverse("user_get_update_api")

        def test_user_retrieve_without_valid_token(self):
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        def test_user_retrieve_with_valid_token(self):
            token = Token.objects.get(user__username="TestUser")
            self.client.credentials(HTTP_AUTHORIZATION=f"token {token.key}")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_user_data_update(self):
            first_name = faker.first_name()
            last_name = faker.last_name()
            token = Token.objects.get(user__username="TestUser")
            self.client.credentials(HTTP_AUTHORIZATION=f"token {token.key}")
            fake_data_to_update = {"first_name": first_name, "last_name": last_name}
            response = self.client.put(url, data=fake_data_to_update, format="json")
            fake_data_after_update = {"first_name": first_name, "last_name": last_name}
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            updated_data = {
                "first_name": response.json().get("first_name"),
                "last_name": response.json().get("last_name"),
            }
            self.assertEqual(updated_data, fake_data_after_update)

        test_user_retrieve_without_valid_token(self)
        test_user_retrieve_with_valid_token(self)
        test_user_data_update(self)
