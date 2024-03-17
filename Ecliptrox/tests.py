from django.test import TestCase
from .forms import StoryForm
# Create your tests here.
from django.urls import reverse

class AddStoryViewTest(TestCase):
    def test_view_url_exists(self):
        response = self.client.get('/add-story/')
        self.assertEqual(response.status_code, 200)
        
        
         # Verifies that the correct form was passed to the rendering context
        self.assertIsInstance(response.context['form'], StoryForm)

        # Tests submission of valid input data
        response = self.client.post('/add-story/', {
            'title': 'A Title',
            'content': 'Some Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertTrue(response.url.startswith('/stories'))  # Correct redirect location