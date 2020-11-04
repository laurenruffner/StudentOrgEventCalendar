from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from eventviewer.models import Event

class eventDeleteView(DeleteView):
    model = Event
    template_name = "event/event_delete.html"
    success_url = reverse_lazy('event_list')