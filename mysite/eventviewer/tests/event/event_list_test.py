from django.test import TestCase
from django.urls import reverse

class eventListTestCase(TestCase):
    def setUp(self):
        pass

    def test_event_list_page(self):
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/event_list.html')