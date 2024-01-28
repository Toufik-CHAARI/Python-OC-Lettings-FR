from django.test import TestCase
from django.urls import reverse


'''
class ErrorViewTestCase(TestCase):

    def test_500_error(self):
        response = self.client.get(reverse('test_500_error_view_name'))
        self.assertEqual(response.status_code, 500)
'''
class IndexViewTestCase(TestCase):
    def test_index_view(self):
        # Call the index view
        url = reverse('index')
        response = self.client.get(url)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class IndexViewIntegrationTestCase(TestCase):
    def test_index_view(self):
        # Get the URL for the index view using the reverse function
        url = reverse('index')

        # Make a GET request to the index view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'index.html')