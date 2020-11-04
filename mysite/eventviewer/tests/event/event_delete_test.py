from django.test import TestCase
from django.urls import reverse

class eventDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_event_delete_page(self):
        response = self.client.get(reverse('event_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/event_delete.html')