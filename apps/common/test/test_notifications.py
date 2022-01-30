# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from faker import Faker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

# project imports
from apps.common.models import Notification as NotificationModel
from apps.common.test.common_test_helper import populate_test_db

# Create your tests here.

faker = Faker("cz_CZ")


class TestNotification(APITestCase):
    def setUp(self):
        super().setUp()
        populate_test_db(model={"notification"})

    def test_notifications_list_api(self):
        url = reverse("notifications_list_api")

        def test_notifications_list_api_denied(self):
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        def test_notifications_list_api_success(self):
            token = Token.objects.get(user__username="TestUser")
            self.client.credentials(HTTP_AUTHORIZATION=f"token {token.key}")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        test_notifications_list_api_denied(self)
        test_notifications_list_api_success(self)

    def test_retrieve_delete_notification_api(self):
        notification = NotificationModel.objects.filter(user__username="TestUser").first()
        url = reverse("notification_api", kwargs={"pk": notification.id})

        def test_retrieve_notification_api_success(self):
            token = Token.objects.get(user__username="TestUser")
            self.client.credentials(HTTP_AUTHORIZATION=f"token {token.key}")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_retrieve_notification_api_denied(self):
            self.client.credentials()
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        def test_retrieve_notification_api_not_found(self):
            url = reverse("notification_api", kwargs={"pk": 0})
            token = Token.objects.get(user__username="TestUser")
            self.client.credentials(HTTP_AUTHORIZATION=f"token {token.key}")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_delete_notification_api_success(self):
            token = Token.objects.get(user__username="TestUser")
            self.client.credentials(HTTP_AUTHORIZATION=f"token {token.key}")
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        def test_delete_notification_api_not_found(self):
            token = Token.objects.get(user__username="TestUser")
            self.client.credentials(HTTP_AUTHORIZATION=f"token {token.key}")
            url = reverse("notification_api", kwargs={"pk": 0})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        test_retrieve_notification_api_success(self)
        test_retrieve_notification_api_denied(self)
        test_retrieve_notification_api_not_found(self)
        test_delete_notification_api_success(self)
        test_delete_notification_api_not_found(self)

    def test_register_device_api(self):
        url = reverse("register_device_api")

        def test_register_device_api_success(self):
            response = self.client.post(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        def test_register_device_api_not_found(self):
            response = self.client.post(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        test_register_device_api_success(self)
        test_register_device_api_not_found(self)

    def test_notification_api_denied(self):
        def test_delete_notification_api_denied(self):
            url = reverse("notification_api", kwargs={"pk": 0})
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        test_delete_notification_api_denied(self)
