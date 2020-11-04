from django.test import TestCase
from django.urls import reverse

class OrganizationDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_organization_delete_page(self):
        response = self.client.get(reverse('organization_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organization/organization_delete.html')