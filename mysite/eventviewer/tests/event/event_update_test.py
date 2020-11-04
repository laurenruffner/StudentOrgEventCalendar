from django.test import TestCase
from django.urls import reverse

class eventUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_event_update_page(self):
        response = self.client.get(reverse('event_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/event_update.html')