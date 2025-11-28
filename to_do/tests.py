from django.test import TestCase, override_settings
from django.test.client import Client
from http import HTTPStatus


# Create your tests here.

class IPBlackListMiddleware(TestCase):
    def setUp(self):
        self.client = Client()


    @override_settings(BANNED_IPS=None)
    def test_request_successful_without_black_list_setting(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


    @override_settings(BANNED_IPS=['192.168.1.2'])
    def test_request_successful_with_none_blacklisted_setting(self):
        response = self.client.get('/', REMOTE_ADDR='192.168.1.1')
        self.assertEqual(response.status_code, HTTPStatus.OK)


    @override_settings(BANNED_IPS=['192.168.1.2'])
    def test_request_failed_with__blacklisted_setting(self):
        response = self.client.get('/', REMOTE_ADDR='192.168.1.2')
        self.assertEqual(response.status_code, HTTPStatus.OK)


