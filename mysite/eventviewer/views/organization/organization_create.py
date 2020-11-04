from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from eventviewer.models import Organization

class OrganizationCreateView(CreateView):
    model = Organization
    fields = '__all__'
    template_name = "organization/organization_create.html"
    success_url = reverse_lazy('organization_list')
