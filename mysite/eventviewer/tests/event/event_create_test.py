from django.test import TestCase
from django.urls import reverse

class eventCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_event_create_page(self):
        response = self.client.get(reverse('event_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/event_create.html')