from django.test import TestCase
from django.urls import reverse

class eventDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_event_detail_page(self):
        response = self.client.get(reverse('event_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/event_detail.html')