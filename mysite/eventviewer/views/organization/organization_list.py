from django.views.generic import ListView

from eventviewer.models import Organization

class OrganizationListView(ListView):
    model = Organization
    template_name = "organization/organization_list.html"
