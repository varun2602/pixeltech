from django.test import TestCase, Client

# Create your tests here.
import json
import requests_mock
from django.urls import reverse

class ResultViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('result')
        
    @requests_mock.Mocker()
    def test_result_view(self, mock_requests):
        # Create a mock response from the external API
        mock_data = {'user_name': 'varun'}
        
        mock_requests.get('https://pixeltech.onrender.com/img/get_data/', json=mock_data)
        
        # Make a GET request to the result view
        response = self.client.get(self.url)
        
        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Assert that the response content contains the expected data from the mock response
        expected_data = json.dumps(mock_data)
        self.assertContains(response, expected_data)
        
        # Assert that the response is rendered using the result.html template
        self.assertTemplateUsed(response, 'result.html')
