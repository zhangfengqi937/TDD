from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from django.template.loader import render_to_string

from tombApp.views import home_page 
from tombApp.models import Item
import unittest
# Create your tests here.
class HomePageTest(TestCase):
    @unittest.SkipTest
    def testHomePage(self):
        found = resolve('/')    #root page, or webroot, no folder 127.0.0.1:8000
        self.assertEqual(found.func, home_page, 'Home page resolves incorrectly')

#check content of a home page

    @unittest.SkipTest
    def testHomePageH1(self):
        request = HttpRequest()
        response = home_page(request)   #all the HTML
        html = response.content.decode('utf8') #convert to human readable HTML
        self.assertIn('<h1>Welcome to the Tomb of Horror</h1>', html, 'H1 contents fail')

#check for smoke test
@unittest.SkipTest
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

#check for homepage
class HomePageTestTxt(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    @unittest.SkipTest
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTure(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
    
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first(ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first(ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')