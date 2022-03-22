from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class StaticURLTests(TestCase):
    """ URL tests """
    def setUp(self):
        """ setting up common conditions for all tests """
        self.guest_client = Client()

        self.user = User.objects.create(username="test_user")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
    

    def test_pages_return_correct_statuses_unauthorized(self):
        """ checking for correct templates for unauthorized client """
        status_codes = {
            200: reverse("home"),
            200: reverse("register"),
            200: reverse("login"),
            302: reverse("logout"),
        }
        for status_code, reverse_name in status_codes.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertEqual(response.status_code, status_code)

    def test_pages_return_correct_statuses_authorized(self):
        """ checking for correct templates for authorized client """
        status_codes = {
            200: reverse("home"),
            302: reverse("register"),
            302: reverse("login"),
            302: reverse("logout"),
        }
        for status_code, reverse_name in status_codes.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertEqual(response.status_code, status_code)
