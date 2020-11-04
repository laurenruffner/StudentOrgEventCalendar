from django.views.generic import DetailView

from eventviewer.models import Organization


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization/organization_detail.html"
