from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from tasks.views import home_page


# Testing HomePage
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/tasks/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>ClockWise</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
