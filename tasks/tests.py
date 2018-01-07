from django.urls import resolve
from django.test import TestCase
from tasks.views import home_page


# Testing HomePage
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/tasks/')
        self.assertEqual(found.func, home_page)
