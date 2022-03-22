from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class PageViewsTests(TestCase):
    """ URL tests """
    def setUp(self):
        """ setting up common conditions for all tests """
        self.guest_client = Client()

        self.user = User.objects.create(username="test_user")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
    
    def test_pages_use_correct_templates_unauthorized(self):
        """ checking for correct templates for unauthorized client """
        templates_pages_names = {
            'index.html': reverse("home"),
            'register.html': reverse("register"),
            'login.html': reverse("login"),
        }
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.guest_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
    
    def test_pages_use_correct_templates_authorized(self):
        """ checking for correct templates for authorized client """
        templates_pages_names = {
            'index.html': reverse("home"),
        }
        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
