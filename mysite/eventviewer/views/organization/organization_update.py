from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from eventviewer.models import Organization

class OrganizationUpdateView(UpdateView):
    model = Organization
    fields = '__all__'
    template_name = "organization/organization_update.html"
    success_url = reverse_lazy('organization_list')
