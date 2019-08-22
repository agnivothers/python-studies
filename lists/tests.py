from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

#class SmokeTest(TestCase):
#  def test_bad_maths(self):
#    self.assertEqual(1+1,2)

class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html_old(self):
    request = HttpRequest()
    response = home_page(request)
    html = response.content.decode('utf8')
    self.assertTrue(html.startswith('<html>'))
    self.assertIn('<title>To-Do lists</title>',html)
    self.assertTrue(html.strip().endswith('</html>'))

  def test_home_page_returns_correct_html(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response,'home.html')
